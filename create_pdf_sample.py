from ho import pisa


def create_pdf(file_name, html):
    with open(file_name, 'wb') as doc:
        pdf = pisa.CreatePDF(html, doc)
        if not pdf.err:
            pisa.startViewer(file_name)

if __name__ == '__main__':
    create_pdf('sample_pdf.pdf', """
    <html>
    <head>
        <style type="text/css">
            #greeting { background-color:#0cc; text-align:center; padding:10px;}
            .table_header {background-color:#00c; text-align:left; padding:5px;}
            .number_table_data {background-color:#0c0; text-align:right; padding:1px;}
        </style>
    </head>
    <body>
        <div id="greeting">Hello There</div>
        <div>
        <table>
        <tr>
            <th class="table_header">First</th>
            <th class="table_header">Second</th>
            <th class="table_header">Third</th>
            <th class="table_header">Fourth</th>
            <th class="table_header">Fifth</th>
        </tr>
        <tr>
            <td class="number_table_data">1</td>
            <td class="number_table_data">2</td>
            <td class="number_table_data">3</td>
            <td class="number_table_data">4</td>
            <td class="number_table_data">5</td>
        </tr>
        </table>
        </div>
    </body>
    </html>
    """)