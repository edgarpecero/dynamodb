def lambda_handler(event, context):
    try:
      for record in event['Records']:
        if record['eventName'] == 'MODIFY':
            handle_update(record)
        if record['eventName'] == 'INSERT':
            handle_insert(record)
        if record['eventName'] == 'REMOVE':
            handle_remove(record)
    except Exception as e:
      print(e)
      return 'Error'

    return 'Ready!'
  
def handle_insert(record):
    print('NEW INSERT EVENT')
    print(record)
    
def handle_update(record):
    print('NEW MODIFY EVENT')
    print(record)
    
def handle_remove(record):
    print('NEW REMOVE EVENT')
    print(record)
    