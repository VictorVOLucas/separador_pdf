import PyPDF2

# def extrair_paginas(input_pdf, prefixo_output):
def extrair_paginas(input_pdf):
    # Abre o arquivo PDF original
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_paginas = len(pdf_reader.pages)

        # Itera através de todas as páginas em pares (2 em 2)
        for pagina_num in range(0, total_paginas, 2):
            # Cria um novo arquivo PDF para cada par de páginas
            output_pdf = f"pagina_{pagina_num + 1}_{pagina_num + 2}.pdf"

            with open(output_pdf, 'wb') as output_file:
                pdf_writer = PyPDF2.PdfWriter()

                # Adiciona as duas páginas ao novo arquivo
                pdf_writer.add_page(pdf_reader.pages[pagina_num])
                
                # Verifica se há uma próxima página antes de adicionar
                if pagina_num + 1 < total_paginas:
                    pdf_writer.add_page(pdf_reader.pages[pagina_num + 1])

                # Salva o novo arquivo PDF
                pdf_writer.write(output_file)

# if __name__ == "__main__":
#     input_pdf = "separado.pdf"
#     extrair_paginas('separado.pdf')
