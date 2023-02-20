import requests


def positive_numbers(func):
    def wrapper(*args):
        result = func(*args)
        if result < 0:
            result = 0
        return result
    return wrapper


@positive_numbers
def sub(a, b):
    return a - b


def retry(num):
    def decorator(func):
        def wrapper(*args):
            count = 0
            result = None
            while num > count:
                try:
                    result = func(*args)
                    break
                except:
                    print(f'Попытка {count + 1} не удачна')
                    count += 1
            return result
        return wrapper
    return decorator


@retry(5)
def get_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content


url = "https://exa1mple.com"
content = get_url(url)
print(content)
