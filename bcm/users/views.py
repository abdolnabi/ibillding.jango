from django.shortcuts import render, redirect

from users.forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
        return redirect('users:login')

    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
import json
import requests
import urllib,urllib3
def landing_page(request):
    # data = {
    #     'url': 'http://blog.ibillding.com/wp-json/wp/v2/posts',
    # }
    # with urllib.request.urlopen('http://blog.ibillding.com/wp-json/wp/v2/posts') as response:
    #     source = response.read()
    #     data = json.loads(source)
    # json_obj = urllib.re.urlopen(url)
    # data = json.load(json_obj)
    response = requests.get('http://blog.ibillding.com/wp-json/wp/v2/posts?_embed')
    data1 = response.json()

    response2 = requests.get('http://blog.ibillding.com/wp-json/wp/v2/media')
    data_image = response2.json()
    # for post in data1:
    #     post_image= post[_embedded]['wp:featuredmedia']['0'][source_url]

    data = {
        'posts' : data1,
        'image_post': data_image
    }
    # return render(request, 'core/home.html', {
    #     'ip': geodata['ip'],
    #     'country': geodata['country_name'],
    #     'latitude': geodata['latitude'],
    #     'longitude': geodata['longitude'],
    #     'api_key': 'AIzaSyC1UpCQp9zHokhNOBK07AvZTiO09icwD8I'
    # # Don't do this! This is just an example. Secure your keys properly.
    # })
    # results = []
    # for item in data:
    #     results.append({
    #         'status': item['status'],
    #         'device': item['device'],
    #     })
    # return render(request, 'index/index.html', {'objects_list': results})
    return render(request, 'landing/index.html',data)
