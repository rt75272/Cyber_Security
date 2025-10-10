import pandas as pd

# Sample login data with user information
logs = pd.DataFrame({
    'user_id': [101, 102, 103],
    'ip_address': ['192.168.1.5', '192.168.1.6', '192.168.1.7'],
    'login_time': ['2025-10-10 09:32', '2025-10-10 09:47', '2025-10-10 10:12']
})

# Mask IP addresses to anonymize user data
logs['ip_address'] = logs['ip_address'].apply(lambda x: '***.***.***.' + x.split('.')[-1])
print(logs)
