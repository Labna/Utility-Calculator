# Utility-Calculator
 a usefull python command line calculator


## simple use
To use it simply, in a command line run 
``` > python -i calculator.py ```
Then, you get the message 
> Calculator charged !

and python invite you to interact :
``` >>> ```

to get help use :
``` >>> calculator('help') ```

#### exemples
1.
```python
>>> calculator("9h52m10s = s")
35530.0s 
```
2.
```python
>>> calculator('82280s - 39713s')
11h49m27s
```
3.
```python
>>> calculator('help')
write operation like :
  5 + 5
  15 8 + 21 (the 2nd number (8) is the base)
  438m = h (get the decimal value of hour, otherwise get full convertion (like : 1y2d3h4m5s6ms)
  5h31m0s145ms + 2y4d18h32m42s + 4h32s + 484s (time operation is possible (the order is : CDydhmsms Century Decade year day hour minute second milisecond (ms is the only 2 char unit))
  45 13 * 12 4 = 16 (the answer will be converted by the base mentionned after the =)
  newDic (to change current dicNumber)
  curDic (to get current dicNumber)
press enter to leave (empty entry)
As second argument you can change the number dictionnary
  (default) calculator("Exemple 62 + of 62 + Calcul 62 = 19", "safe") ->  safe=[0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
  calculator("def 26", "min") -> min=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
  calculator("SPQR 26", "maj") -> maj=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
  calculator(newDicNumber="invert") -> invert=[0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
  calculator(newDicNumber="base64") -> base64=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9,+,/]
  or you can use yours, exemple: "calculator("PONY 26", newDicNumber=['Z','X','Y','P','W','V','U','T','S','R','Q','I','M','L','K','J','N','H','G','F','O','E','D','C','B','A']"
  if a number is out of the dictionnary size it can be introduce with the [] as : calculator("[27][38]5[18] 64 = 10")
  the dictionnary is kept for future use into global variable : dicNumber
As third argument you can change the output behaviour
  (default) calculator("7794075 = 62", clear=False) -> print the result in the stdout
  calculator("7794075 = 62", clear=True) to return the string as output of the function
```

## Version review :
V1.1 : add bracket support '() [] {}'

```python
>>> calculator("( 34384s - 2550s ) * ( 25433 / 83460s )")
2h41m40s864ms
```

V1.2 : add fractionnal values supprt (like: '5.5  3.1415')

```python
>>> calculator("5.5 10 = 16")
5.8 base: 16
```

V1.2.1 : a quiet parameter wasn't implemented (and other fixes)

now you can choose between get the result into the console (clear=False (default))
or to get the result (only the string of the number without the base) (clear=True)

```python
>>> a = calculator("5.2 10 + 38.6 9 * 599046 64 = 16", clear=True)
>>> a
'2DDB5979DB.33333'
```

Note pour les tests de performances
```python
>>> import time;time1 = time.time(); a = [calculator("5.2 10 + 38.6 9 * 599046 64 = 16", clear=True) for x in range(10000)] ;time2 = time.time();print((time2-time1)*1000)
1427.6394 (ms)
```

