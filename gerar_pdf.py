import pandas as pd
from fpdf import FPDF

# Carregar dados da planilha
df = pd.read_excel("cupons.xlsx")  # Certifique-se de que o nome do arquivo está correto

# Configurar o modelo de PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Cupom Promocional", ln=True, align="C")
    
    def add_coupon(self, code1, code2):
        self.set_font("Arial", "", 12)
        self.ln(20)
        self.cell(0, 10, f"Código 1: {code1}", ln=True)
        self.cell(0, 10, f"Código 2: {code2}", ln=True)
        self.ln(10)

# Gerar PDFs
for index, row in df.iterrows():
    pdf = PDF()
    pdf.add_page()
    pdf.add_coupon(row["Codigo1"], row["Codigo2"])
    pdf.output(f"cupom_{index + 1}.pdf")