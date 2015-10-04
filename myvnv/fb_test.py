import facebook
import requests
from sys import argv

file_name = argv[1]
fp = open(file_name,'r+')
contents = [line.strip('\n') for line in fp]

token = 'YOUR_ACCESS_TOKEN'
g = facebook.GraphAPI(token)
profile = g.get_object("me")

Posts = g.get_connections("me", "Posts")
i=0  #counter
p_wish = ['bday','birthday']
messg_id = []
count = 0
for Post in Posts['data']:
  if "2015-10-0" in Post["created_time"] and Post['id'] not in contents:
    try:
      messg = Post['message'].lower()
      found = False

      for item in p_wish:
        if item in messg:
          found = True

      if found:
        messg_id.append(Post['id'])
    except KeyError:
      continue
    if count == 20:
      break
    else:
      count +=1 

#g = facebook.GraphAPI(access_token=token)#, version='2.4')

#g.put_wall_post(profile_id='me',message='Hello')
print (messg_id)
for value in messg_id:
  g.put_comment(object_id=value, message='Thanks for the wishes :)'+'\n\n'+'.'+'\n\n'+'(This is an automated reply, I will get back to you once i come online)')
  if g.put_like(object_id=value):
    print('done')


#Appending Record
messg_id += contents

#Updating Record
fp = open(file_name,'w+')
for m in messg_id:
    fp.write(m+'\n')
fp.close

