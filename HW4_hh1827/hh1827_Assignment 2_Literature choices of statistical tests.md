# FBB I asked for this to be in the folder README, not in a separate markdown. PLease read instructions carefully



| **Statistical Analyses | IV(s) | IV type(s)  |DV(s)  | DV type(s) | Control Var  | Control Var type | Question to be answered | _H0_ | alpha | link to paper ** |
| ------ |:--------:| -----:| ------:| ------:| ------:| ------:| ------:| ------:| ------:| ------:|
| Logistic Regression | 7, BMI, TA/systole, TA/diastole, liver right lobe, hilus big, hilus down, lung arbrz | Categorical | 1,diagnosed as obisity or no | Categorical | 0 | NA | Diagnosing whether a subject is obese according to his/her performance in terms of given medical parameters | Logit p(healthy 0, obese 1) != a*BMI + b*TA systole + c*TA diastole + d*liver right lobe + e*hilus down + f*hilus big g*lung arbrz| 0.05 | [The Classification of Obesity Disease in Logistic Regression and Neural Network Methods](https://link.springer.com/article/10.1007%2Fs10916-008-9165-5#Sec6) | | 
| Correlation	| 1,Income Inequality | Continuous | 1,Antimicrobial Resistance| continuous | 0 | 0 | 	 If correlations exist between income inequality and antimicrobial resistance. |The level of pins expression in test groups >= Ranks control group   | 0.05 | [Correlations between Income Inequality and Antimicrobial Resistance](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0073115) |
|MANOVA                   |1,Anthropometric variables(Height, Weight and Age)                                    2.Five single motor tests(Sprint,Agility,Dribbling,Ball control,Shooting)           |Continuous        |1,Adult performance level (APL) of players in 15/16 season      |Continuous        |None      |None          |Gain the predictive motor tests’ prognostic relevance in talent development programs in youth soccer|the predictive motor tests’ prognostic relevance in talent development programs in youth soccer are similar           |0.05      |[The influence of speed abilities and technical skills in early adolescence on adult success in soccer: A long-term prospective analysis using ANOVA and SEM approaches](http://journals.plos.org/plosone/article?id=10.1371/journa

## FBB 
### MANOVA: confusing: IV and DV are swapped. IV is the performance level, DV is the biometrics and test performance.The question as formulated I am not sure I understand it, but from the paper it is "are the youth tests predictors of performance in adult age?" and the H0 that the tests for all APL (performance group levels) will be the same
## otherwise ok (though the nulls could be simplified in the other tests


```python

```
