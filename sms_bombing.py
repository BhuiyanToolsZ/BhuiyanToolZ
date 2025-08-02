try:
    import sms_bombing
    sms_bombing.start()
except Exception as e:
    print(f"Error: {e}")