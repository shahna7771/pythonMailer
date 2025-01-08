import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendmail(workflow_name, repo_name,workflow_run_id):
  #email details
  sender_email= os.getenv('SENDER_EMAIL')
  sender_password= os.getenv('SENDER_PASSWORD')
  receiver_email= os.getenv('RECEIVER_EMAIL')

  subject = f"workflow {workflow_name} failed for repo {repo_name} "
  body = f"Hi, the workflow {workflow_name} failed for repo {repo_name} .Please check the logs for more details. \n More Details: \nRunId: {workflow_run_id}"

  msg = MIMEMultipart()
  msg['FROM'] = sender_email
  msg['TO'] = receiver_email
  msg['Subject'] =subject
  msg.attach(MIMEText(body,'plain'))
  
  try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email,sender_password)
    text = msg.as_string()
    server.sendmail(sender_email,receiver_email,text)
    server.quit()

    print ('email sent successfully')
  except Exception as e :
    print( f'Error:{e}')
    
sendmail(os.getenv('workflow_name'),os.getenv('repo_name'),os.getenv('workflow_run_id'))