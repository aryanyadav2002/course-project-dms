# from io import BytesIO
# from logging import exception
# from urllib import response
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa  
# import uuid
# from django.conf import settings


# # defining the function to convert an HTML file to a PDF file
# def html_to_pdf(params:dict):
#     template = get_template('dgbbop.html')
#     html  = template.render(params)
#     response = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
#     file_name=uuid.uuid4()
#     try:
#         with open(str(settings.BASE_DIR)+ f'{file_name}.pdf', 'wb+') as output:
#             pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), output)
    
#     except Exception as e:
#         print(e)


#     if not pdf.err:
#         return '' , False
#     return file_name , True