class Sol:
    def licenseKeyFormatting(self,s,k):
        list=[]
        key=s.replace('-','').upper()
        first_group_len=len(key)%k
        if first_group_len!=0:
            list.append(key[0:first_group_len])
        i=first_group_len
        while i<len(key):
            list.append(key[i:i+k])
            i+=k
        return "-".join(list)
