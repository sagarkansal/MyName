try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# code to search 
query = "Abdul Kalam Azad"
 
for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
    print(j)
