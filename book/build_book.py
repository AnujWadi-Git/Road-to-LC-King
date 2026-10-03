"""Builds Python_Fluency_Book.pdf, one concept per page (dark theme).
Run from repo root:  python3 book/build_book.py
"""
import ast
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content import CONCEPTS, QUIZ, TEMPLATE  # noqa: E402
from reportlab.lib import colors  # noqa: E402
from reportlab.lib.pagesizes import letter  # noqa: E402
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
from reportlab.lib.units import inch  # noqa: E402
from reportlab.platypus import (BaseDocTemplate, Frame, KeepInFrame, PageBreak,  # noqa: E402
                                PageTemplate, Paragraph, Preformatted, Spacer, Table, TableStyle)

OUT = os.path.join(os.path.dirname(__file__), "..", "Python_Fluency_Book.pdf")
W, H = letter
M = 0.6 * inch
FW, FH = W - 2 * M, H - 2 * M - 0.1 * inch

BG = colors.HexColor("#12161f")
TXT = colors.HexColor("#e3e8f0")
DIM = colors.HexColor("#9aa6bb")
BLUE = colors.HexColor("#6fa8ff")
CODEBG = colors.HexColor("#1e2636")
LINE = colors.HexColor("#33405a")
AMBER = colors.HexColor("#ffd479")
GREEN = colors.HexColor("#7ee0a1")
PINK = colors.HexColor("#ff9db5")

S = {}
S["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=10.6, leading=14.4, textColor=TXT)
S["dim"] = ParagraphStyle("dim", parent=S["body"], textColor=DIM, fontSize=9.5)
S["kicker"] = ParagraphStyle("kicker", fontName="Helvetica-Bold", fontSize=8.5, textColor=DIM, leading=11)
S["title"] = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=21, leading=25, textColor=colors.white,
                            spaceAfter=2)
S["label"] = ParagraphStyle("label", fontName="Helvetica-Bold", fontSize=9.8, textColor=BLUE, leading=12,
                            spaceBefore=12, spaceAfter=5)
S["code"] = ParagraphStyle("code", fontName="Courier", fontSize=9.3, leading=12, textColor=colors.HexColor("#d7e3f7"),
                           backColor=CODEBG, borderPadding=(5, 7, 5, 7), spaceBefore=4, spaceAfter=9, leftIndent=6,
                           rightIndent=6)
S["req"] = ParagraphStyle("req", parent=S["body"], fontName="Helvetica-Oblique", fontSize=10.8, leading=14.6, textColor=colors.white,
                          backColor=colors.HexColor("#1d2a44"), borderPadding=(5, 7, 5, 7), spaceBefore=2, spaceAfter=4,
                          leftIndent=6, rightIndent=6)
S["tip"] = ParagraphStyle("tip", parent=S["body"], fontSize=9.8, leading=13, leftIndent=10, bulletIndent=0)
S["step"] = ParagraphStyle("step", parent=S["body"], fontSize=10, leading=13.4, leftIndent=14, bulletIndent=2)
S["try"] = ParagraphStyle("try", parent=S["body"], fontSize=10, leading=13.6, leftIndent=18, bulletIndent=0)
S["cell"] = ParagraphStyle("cell", parent=S["body"], fontSize=9.8, leading=12.8)
S["big"] = ParagraphStyle("big", fontName="Helvetica-Bold", fontSize=34, leading=40, textColor=colors.white)
S["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=BLUE, spaceBefore=8,
                         spaceAfter=3)
S["quiz"] = ParagraphStyle("quiz", parent=S["body"], fontSize=8.6, leading=11)
S["quizc"] = ParagraphStyle("quizc", parent=S["quiz"], fontName="Courier", fontSize=8.2, textColor=GREEN)


def fmt(text):
    """Escape, then turn `code` into amber Courier."""
    t = html.escape(text, quote=False)
    return re.sub(r"`([^`]+)`", r'<font name="Courier" color="#ffd479">\1</font>', t)


def pre(code_text):
    return Preformatted(code_text.strip("\n"), S["code"])


def labelled(text, color=BLUE):
    st = ParagraphStyle("l", parent=S["label"], textColor=color)
    return Paragraph(text, st)


def box(flowables, bg, border, width=None):
    t = Table([[flowables]], colWidths=[width or FW])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LINEBEFORE", (0, 0), (0, -1), 2.5, border),
                           ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                           ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return t


LEVEL = {"M": ("MICRO", GREEN), "C": ("COMBO", AMBER), "R": ("REAL", PINK)}
shrink_report = []


def concept_page(n, c):
    f = []
    f.append(Paragraph(f"{c['part']}  |  CONCEPT {n}", S["kicker"]))
    f.append(Paragraph(html.escape(c["title"]), S["title"]))
    f.append(Paragraph(fmt(c["idea"]), S["body"]))

    f.append(labelled("KNOW THIS"))
    f.append(pre(c["know"]))

    f.append(labelled("HOW A QUESTION IS SOLVED  (the process you will copy every time)", GREEN))
    f.append(Paragraph("&ldquo;" + html.escape(c["req"]) + "&rdquo;", S["req"]))
    io = Table([[Paragraph("<b>Inputs:</b> " + fmt(c["inputs"]), S["cell"]),
                 Paragraph("<b>Output:</b> " + fmt(c["output"]), S["cell"])]], colWidths=[FW * 0.5, FW * 0.5])
    io.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 2),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 2), ("LINEBELOW", (0, 0), (-1, 0), 0.4, LINE)]))
    f.append(io)
    f.append(Paragraph("<b>Steps by hand (pseudocode)</b>", ParagraphStyle("x", parent=S["cell"], spaceBefore=3)))
    for i, s in enumerate(c["steps"], 1):
        f.append(Paragraph(fmt(s), S["step"], bulletText=f"{i}."))
    f.append(Paragraph("<b>Python</b>", ParagraphStyle("x2", parent=S["cell"], spaceBefore=3)))
    f.append(pre(c["code"]))

    tips = [Paragraph("TIPS AND TRAPS", ParagraphStyle("tt", parent=S["label"], textColor=AMBER, spaceBefore=0))]
    for t in c["tips"]:
        tips.append(Paragraph(fmt(t), S["tip"], bulletText="•"))
    f.append(Spacer(1, 4))
    f.append(box(tips, colors.HexColor("#2b2616"), AMBER))

    tr = [Paragraph("NOW YOU TRY  (close this page, blank file, no peeking)",
                    ParagraphStyle("tr", parent=S["label"], textColor=PINK, spaceBefore=0))]
    for i, (lvl, q) in enumerate(c["tryit"], 1):
        name, col = LEVEL[lvl]
        tr.append(Paragraph(f'<font color="#{col.hexval()[2:]}"><b>{name}</b></font>  ' + fmt(q), S["try"],
                            bulletText=f"{i}."))
    f.append(Spacer(1, 4))
    f.append(box(tr, colors.HexColor("#2a1b24"), PINK))

    kif = KeepInFrame(FW, FH, f, mode="shrink")
    return kif


def front_matter():
    pages = []
    # cover
    f = [Spacer(1, 1.3 * inch),
         Paragraph("Python Fluency", S["big"]),
         Paragraph("From English requirement to working code", ParagraphStyle("sub", parent=S["body"], fontSize=14,
                                                                             leading=19, textColor=DIM)),
         Spacer(1, 0.4 * inch),
         Paragraph("One concept per page. Every page has the same four parts:", S["body"]),
         Spacer(1, 6)]
    for lab, col, txt in [("KNOW THIS", BLUE, "the syntax to memorize"),
                          ("HOW A QUESTION IS SOLVED", GREEN, "requirement -> inputs -> output -> steps -> Python"),
                          ("TIPS AND TRAPS", AMBER, "what goes wrong and how to avoid it"),
                          ("NOW YOU TRY", PINK, "four questions, micro to real, no solutions in this book")]:
        f.append(Paragraph(f'<font color="#{col.hexval()[2:]}"><b>{lab}</b></font> - {txt}', S["body"]))
        f.append(Spacer(1, 4))
    f.append(Spacer(1, 0.4 * inch))
    f.append(Paragraph("Road to LC King", S["dim"]))
    pages.append(KeepInFrame(FW, FH, f, mode="shrink"))

    # how to use
    f = [Paragraph("START HERE", S["kicker"]), Paragraph("How to use this book", S["title"]),
         Paragraph("Understanding a page is worth nothing. Only code you write yourself counts.", S["body"]),
         labelled("THE LOOP FOR EVERY PAGE"),
         ]
    for i, s in enumerate([
        "Read KNOW THIS once. Then close the book and write the syntax from memory in a blank file.",
        "Read the worked requirement. COVER the solution. Do inputs, output and steps yourself first.",
        "Write the code. Run it. Compare with the book only AFTER your own attempt.",
        "Read TIPS AND TRAPS. These are your most likely bugs.",
        "Do the four NOW YOU TRY questions from a BLANK file. Micro first, real requirement last.",
        "Stuck? Do not look at the answer. Ask: what do I receive, what do I return, what would I do by hand?",
        "Log each mistake in ERROR_LOG.md. Review it before the next session."], 1):
        f.append(Paragraph(fmt(s), S["step"], bulletText=f"{i}."))
    f.append(labelled("MASTERY LEVELS (aim for 7 on every concept)", GREEN))
    for i, s in enumerate(["Recognize it", "Explain it", "Write it with a hint", "Write it independently",
                           "Use it in an unfamiliar problem", "Debug it", "Use it under time pressure"], 1):
        f.append(Paragraph(s, S["step"], bulletText=f"{i}."))
    f.append(labelled("DIFFICULTY LADDER", AMBER))
    f.append(Paragraph("MICRO: one operation.  COMBO: 2-3 operations.  SMALL PROGRAM: several concepts.  "
                       "REAL REQUIREMENT: English only, you pick the tools.  INTERVIEW: unfamiliar, no hints.", S["body"]))
    pages.append(KeepInFrame(FW, FH, f, mode="shrink"))

    # method
    f = [Paragraph("START HERE", S["kicker"]), Paragraph("The 10-step method", S["title"]),
         Paragraph("Run this on EVERY problem. Never start with code.", S["body"]), Spacer(1, 6)]
    rows = [["1", "Restate", "Say it in your own words in one sentence."],
            ["2", "Inputs", "What do I receive? What types?"],
            ["3", "Output", "What do I return or print? What type?"],
            ["4", "Rules", "Write every rule as a sentence. Underline boundary words (at least, over, up to)."],
            ["5", "By hand", "Do one example manually with real numbers."],
            ["6", "Tools", "variable? if/elif? loop? list? dict? set? function? (next page)"],
            ["7", "Pseudocode", "4-8 plain-English steps."],
            ["8", "Code", "Turn each pseudocode line into Python."],
            ["9", "Test", "Normal, boundary, empty/zero, one item, invalid."],
            ["10", "Debug", "Print values. The bug is the first line where reality differs from your prediction."]]
    t = Table([[Paragraph(f"<b>{a}</b>", S["cell"]), Paragraph(f"<b>{b}</b>", S["cell"]), Paragraph(c, S["cell"])]
               for a, b, c in rows], colWidths=[0.4 * inch, 1.2 * inch, FW - 1.6 * inch])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                           ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#1d2a44"))]))
    f.append(t)
    f.append(labelled("IF YOU FREEZE", AMBER))
    f.append(Paragraph("Ask yourself, in this order: What information do we receive? What do we need to return? "
                       "What would I do manually with a small example? Then convert each manual step into one line of code. "
                       "Say out loud: &ldquo;Let me do an example by hand first.&rdquo;", S["body"]))
    pages.append(KeepInFrame(FW, FH, f, mode="shrink"))

    # tool picker
    f = [Paragraph("START HERE", S["kicker"]), Paragraph("Which tool does the English point to?", S["title"]),
         Paragraph("Read the requirement and spot these phrases.", S["body"]), Spacer(1, 6)]
    rows = [["if / otherwise / when / unless", "decision", "if / elif / else"],
            ["for each / every / all", "repeat over items", "for x in items:"],
            ["until / as long as / keep asking", "repeat with a stop", "while cond:"],
            ["total / sum / add up", "accumulator", "total += x"],
            ["count how many", "counter", "count += 1"],
            ["largest / smallest / best", "best so far", "if x > best: best = x"],
            ["list of / in order / many values", "list", "nums = []"],
            ["price of X / how many of each", "dictionary", "d[key]"],
            ["duplicate / unique / seen before", "set (or dict)", "seen = set()"],
            ["calculate / reusable / returns", "function", "def f(): return"],
            ["at least / at most / over / under", "comparison + boundary", ">=  <=  >  <"],
            ["and / or / both / either", "boolean logic", "and  or  not"],
            ["first N / last N / every other", "slicing", "a[:N]  a[-N:]  a[::2]"],
            ["cap / never more than", "min()", "min(total, 20)"],
            ["minimum charge / at least $5", "max()", "max(total, 5)"],
            ["each additional / after the first", "subtract the first", "base + rate * (n - 1)"]]
    hdr = [Paragraph("<b>English says</b>", S["cell"]), Paragraph("<b>Think</b>", S["cell"]),
           Paragraph("<b>Python</b>", S["cell"])]
    cc = ParagraphStyle("cc", parent=S["cell"], fontName="Courier", fontSize=8.4, textColor=AMBER)
    t = Table([hdr] + [[Paragraph(html.escape(a), S["cell"]), Paragraph(html.escape(b), S["cell"]),
                        Paragraph(html.escape(c), cc)] for a, b, c in rows],
              colWidths=[FW * 0.40, FW * 0.25, FW * 0.35])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINE), ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#27344f")),
                           ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    f.append(t)
    pages.append(KeepInFrame(FW, FH, f, mode="shrink"))
    return pages


def template_page():
    f = [Paragraph("INTERVIEW  |  TEMPLATE", S["kicker"]), Paragraph("The blank-file template", S["title"]),
         Paragraph("Type this skeleton from memory at the start of any problem. Fill in the blanks. "
                   "It gives you a first move so you never stare at an empty file.", S["body"]),
         labelled("SKELETON"), pre(TEMPLATE),
         labelled("WHAT EACH STEP MEANS", GREEN)]
    for i, s in enumerate(["Edge case first: empty input, zero, one item. Return something sensible.",
                           "Variables: what do I need to remember while looping? total, count, best, a result list, a dict, a set.",
                           "Loop: visit every item (or while until a stop).",
                           "Decide: if/elif for the rule from the requirement.",
                           "Return (or print) exactly what the requirement says.",
                           "Test: normal, boundary, empty."], 1):
        f.append(Paragraph(fmt(s), S["step"], bulletText=f"{i}."))
    return KeepInFrame(FW, FH, f, mode="shrink")


def quiz_pages():
    half = (len(QUIZ) + 1) // 2
    pages = []
    for pi, chunk in enumerate([QUIZ[:half], QUIZ[half:]]):
        f = [Paragraph(f"FLASH DRILL  |  PART {pi + 1}", S["kicker"]),
             Paragraph("Syntax flash drill", S["title"]),
             Paragraph("Cover the right column. Answer from memory, out loud. Every miss goes into ERROR_LOG.md.",
                       S["body"]), Spacer(1, 6)]
        rows = [[Paragraph("<b>#</b>", S["quiz"]), Paragraph("<b>Question</b>", S["quiz"]),
                 Paragraph("<b>Answer</b>", S["quiz"])]]
        for i, (q, a) in enumerate(chunk, 1 + pi * half):
            rows.append([Paragraph(str(i), S["quiz"]), Paragraph(html.escape(q), S["quiz"]),
                         Paragraph(html.escape(a), S["quizc"])])
        t = Table(rows, colWidths=[0.4 * inch, FW * 0.45, FW * 0.55 - 0.4 * inch])
        t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINE), ("BACKGROUND", (0, 0), (-1, 0),
                                                                        colors.HexColor("#27344f")),
                               ("TOPPADDING", (0, 0), (-1, -1), 4.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
                               ("VALIGN", (0, 0), (-1, -1), "TOP")]))
        f.append(t)
        pages.append(KeepInFrame(FW, FH, f, mode="shrink"))
    return pages


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, W, H, stroke=0, fill=1)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#7d8799"))
    canvas.drawString(M, 0.38 * inch, "Road to LC King - Python Fluency")
    canvas.drawRightString(W - M, 0.38 * inch, f"{doc.page}")
    canvas.restoreState()


def check_code():
    bad = 0
    for c in CONCEPTS:
        try:
            ast.parse(c["code"])
        except SyntaxError as e:
            print("SYNTAX ERROR in solved code of", c["title"], e)
            bad += 1
    return bad


def main():
    if check_code():
        sys.exit(1)
    pages = front_matter()
    for n, c in enumerate(CONCEPTS, 1):
        pages.append(concept_page(n, c))
    pages.append(template_page())
    pages.extend(quiz_pages())

    story = []
    for i, p in enumerate(pages):
        if i:
            story.append(PageBreak())
        story.append(p)

    doc = BaseDocTemplate(OUT, pagesize=letter, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M + 0.1 * inch,
                          title="Python Fluency", author="Road to LC King")
    frame = Frame(M, M + 0.1 * inch, FW, FH, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=on_page)])
    doc.build(story)
    for i, pg in enumerate(pages, 1):
        sc = getattr(pg, "_scale", 1)
        if sc < 0.97:
            print(f"page {i}: shrunk to {sc:.2f}")
    print("wrote", os.path.abspath(OUT), "pages:", len(pages))


if __name__ == "__main__":
    main()
