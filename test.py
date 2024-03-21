from requests import get

print(get('http://localhost:5000/api/jobs',).json())
print(get('http://localhost:5000/api/jobs/2').json())
print(get('http://localhost:5000/api/jobs/1234567').json())
print(get('http://localhost:5000/api/jobs/asdfgh').json())