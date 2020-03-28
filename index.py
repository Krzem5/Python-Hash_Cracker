import hashlib
import time



def gen_digit_hash_table(fp,N=0,DIGITS=4):
	def pad(s,l,c):
		while (len(s)<l):
			s=c+s
		return s
	l=-1
	if (N==0):
		with open(fp,"w") as f:
			f.write("code,SHA1,SHA224,SHA256,SHA384,SHA512,MD5\n")
	with open(fp,"a")as f:
		start=time.time()
		while (N<10**DIGITS):
			if (int(N/(10**DIGITS)*100)>l):
				l=int(N/(10**DIGITS)*100)
				print(f"{l}% complete... ({int((time.time()-start)*100)/100}s)")
				start=time.time()
			s=pad(str(N),DIGITS,'0')
			f.write(f"{s},{hashlib.sha1(s.encode('UTF-8')).hexdigest()},{hashlib.sha224(s.encode('UTF-8')).hexdigest()},{hashlib.sha256(s.encode('UTF-8')).hexdigest()},{hashlib.sha384(s.encode('UTF-8')).hexdigest()},{hashlib.sha512(s.encode('UTF-8')).hexdigest()},{hashlib.md5(s.encode('UTF-8')).hexdigest()}\n")
			N+=1
def gen_string_hash_table(i,fp,idx=0):
	l=-1
	if (idx==0):
		with open(fp,"w") as f:
			f.write("string,SHA1,SHA224,SHA256,SHA384,SHA512,MD5\n")
	with open(fp,"a")as f:
		start=time.time()
		while (idx<len(i)):
			if (int(idx/len(i)*100)>l):
				l=int(idx/len(i)*100)
				print(f"{l}% complete... ({int((time.time()-start)*100)/100}s)")
				start=time.time()
			s=i[idx]
			f.write(f"{s},{hashlib.sha1(s.encode('UTF-8')).hexdigest()},{hashlib.sha224(s.encode('UTF-8')).hexdigest()},{hashlib.sha256(s.encode('UTF-8')).hexdigest()},{hashlib.sha384(s.encode('UTF-8')).hexdigest()},{hashlib.sha512(s.encode('UTF-8')).hexdigest()},{hashlib.md5(s.encode('UTF-8')).hexdigest()}\n")
			idx+=1



def crack_hash(f,h,s):
	t=""
	with open(f,"r") as f:
		t=f.read()
	head,t=t.split("\n")[0],t.split("\n")[1:]
	i=head.split(",").index(h.upper()) if h!="" else -1
	for l in t:
		if (l==""):continue
		if (i!=-1):
			if (l.split(",")[i]==s):
				return (l.split(",")[0],h.upper())
		else:
			for j in range(len(head.split(","))):
				if (l.split(",")[j]==s):
					return (l.split(",")[0],head.split(",")[j])
	return (None,None)