from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 24)
        self.cell(0, 10, 'CS50 Shirtificate', ln=True, align='C')

    def add_shirtificate(self, name):
        self.image("shirtificate.png", x=(210-150)/2, y=60, w=150)  # Center the image
        self.set_xy(0, 140)
        self.set_font('Arial', 'B', 36)
        self.set_text_color(255, 255, 255)  # White color
        self.cell(210, 10, name, align='C')  # Centered horizontally

def create_shirtificate(name):
    pdf = PDF()
    pdf.add_page()
    pdf.add_shirtificate(name)
    pdf.output('shirtificate.pdf')

if __name__ == "__main__":
    name = input("Enter your name: ")
    create_shirtificate(name)