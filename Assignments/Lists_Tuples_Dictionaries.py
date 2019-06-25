### Code for get_grades starts here
def get_grade(x,y):
    s=float(x)
    if s>=y["A"]:
        return "A"
    elif s=y["B"]:
        return "B"
    elif s=y["C"]:
        return "C"
    elif s=y["D"]:
        return "D"
    else:
        return "F"
### END MARKER



### Code for get_student_marks starts here
def get_student_marks(l):
    ans_dic={}
    a=l[0]["roll_no"]
    b=l[0]["marks"]
    ini1=0
    ini3=0
    for i in ("english","calculus"):
        c=b[i]
        for j in c:
            if j ==None:
                continue

            if i=="english":
                ini1+=j
                e=i
            elif i=="calculus":
                ini3+=j
                f=i
    ans_dic[a]={e:ini1,f:ini3}
    g=l[1]["roll_no"]
    h=l[1]["marks"]
    total_pf=0
    total_eng=0
    for s in "english","programming fundaments":
        m=h[s]
        for n in m:
            if n==None:
                continue
            if s=="english":
                total_eng=total_eng+n
                p=s
            elif s=="programming fundaments":
                total_pf=total_pf+n
                r=s
    ans_dic[g]={p:total_eng,r:total_pf}
    x1=l[2]["roll_no"]
    y1=l[2]["marks"]
    k1=0
    k2=0
    for v in "calculus","programming fundamentals":
        m1=y1[v]
        for n1 in m1:
            if n1==None:
                continue

            if v=="calculus":
                k1+=n1
                p1=v
            elif v=="programming fundamentals":
                k2+=n1
                r1=v
    ans_dic[x1]={p1:k1,r1:k2}
    return(ans_dic)

### END MARKER



if __name__ == '__main__':
    grade_boundaries = {'A': 80, 'B': 70, 'C': 60, 'D': 50}

    student_data = [
        {'roll_no': 'p18-1001', 'marks': {
                'english': (1.4, 2.5, 15, 9.6, 33),
                'calculus': (2.4, 1.5, 12, 1.6, 21),
            }, 'attendance': 88.4
        },
        {'roll_no': 'p18-1002', 'marks': {
                'english': (2.4, 1.5, 12, 1.6, 21),
                'programming fundaments': (2.4, 1.5, 12, 1.6, 21),
            }, 'attendance': 79.4
        },
        {'roll_no': 'p18-1003', 'marks': {
                'calculus': (2.4, 1.5, 12, None, 21),
                'programming fundamentals': (2.4, 1.5, 12, 1.6, 21),
            }, 'attendance': 79.4
        },
    ]


    # print(student_data)
    student_marks = get_student_marks(student_data)
    print(student_marks)

    print(get_grade(80, grade_boundaries))
