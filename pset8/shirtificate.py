from fpdf import FPDF, Align


# The orientation of the PDF should be Portrait.
# The format of the PDF should be A4, which is 210mm wide by 297mm tall.
# The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.
def main():

    name = input("your name: ").strip()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=30)
    pdf.cell(w=0, h=20, text="CS50 Shirtificate", align="C")
    pdf.ln(20)
    pdf.image("shirtificate.png", x=Align.C, y=50, w=pdf.epw)

    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(140)
    pdf.cell(w=0, h=10, text=f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
