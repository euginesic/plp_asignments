import pandas as pd
import numpy as np
student={
         "name":["eugine","sichangi","mercy"],
         "eng":[78,60,58], 
         "kis":[90,78,10], 
         "math":[66,44,55],
         "geo":[88,22,30],
         "bio":[75,56,29] 
         } 
score=pd.DataFrame(student,index=["student1","student2","student3"])
score["total"]=[389,200,400]
score["coments"]=["good","average","poor"]
new_row=pd.DataFrame([{"name":"juma","eng":58,"kis":80,"math":74,"geo":100,"bio":12,"total":500,"coments":"satisfactory"}],index=["student4"])
new_row2=pd.DataFrame([{"name":"faith","eng":79,"kis":50,"math":66,"geo":100,"bio":40,"total":400,"coments":"very well"}],index=["student5"])
score=pd.concat([score,new_row2])
score=pd.concat([score,new_row])
#score["eng_mean"]=[66.6,61.6,61.0,68.0,42.4]
eng_mean=pd.DataFrame([{"eng":61.6,"kis":61.6,"math":61.0,"geo":68.0,"bio":42.2}],index=["mean"])
score=pd.concat([score,eng_mean])
#print(score)
#eng=score[score["eng"]>60]
#eng=[78,60,58,79,58]
#print( f"\neng mean is :{np.mean(eng)}")
#kis=[90,78,10,50,80]
#print(f"kis mean is :{np.mean(kis)}")
#math=[66,44,55,66,74]
#print(f"math mean is :{np.mean(math)}")
#geo=[88,22,30,100,100]
#print(f"geo mean is :{np.mean(geo)}")
#bio=[75,56,29,40,12]
#print(f"bio mean is :{np.mean(bio)}")

#print(score)
#score.drop(["student1"])
#print(eng)


#print(score.head())
print(score)


student=input(str("enter students index:"))
try:
    print(score.loc[student])
except KeyError:
    print(f"{student} ,does not exist!")
print("data saved to student_scores.csv")