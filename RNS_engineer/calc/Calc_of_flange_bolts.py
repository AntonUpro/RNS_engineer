from math import cos, pi, radians


def calc_F(foundation_bolts,on_bolt,count_bolts,bolt_strength_class,diametr_bolta,circle_diameter,stress_N,stress_M,index_dinamic):
    try:
        circle_diameter=float(circle_diameter)
        count_bolts=float(count_bolts)
        diametr_bolta=int(diametr_bolta)
        stress_N=float(stress_N)
        stress_M=float(stress_M)
    except:
        return 'Ошибка ввода данных'
    
    if foundation_bolts:
        if diametr_bolta<24:
            Fund_G2S=265
        elif diametr_bolta<36:
            Fund_G2S=245
        else:
            Fund_G2S=230
        rasch_sopr_dict={'Ст3':190,"09Г2С":Fund_G2S}
        index_dinamic1=index_dinamic
    else:
        rasch_sopr_dict={'5.6':225,'5.8':225,'8.8':451,'10.9':728,'12.9':854}
        index_dinamic1=1
    square_bolt_bn_dict={12:0.84,16:1.57,18:1.92,20:2.45,22:3.03,24:3.53,27:4.59,30:5.16,36:8.16,42:11.57,48:14.72,56:20.30,64:26.76,72:34.6,80:43.44,90:55.91,100:69.95,110:85.56,125:111.91,140:141.81}
    rasch_sopr=rasch_sopr_dict[bolt_strength_class]
    square_bolt=square_bolt_bn_dict[diametr_bolta]
    radius=circle_diameter/2/1000
    if count_bolts%4==0:
        ug=0
        col_bl=2
        c_1=radius
    elif count_bolts%2==0:
        ug=180/count_bolts
        col_bl=4
        c_1=cos(radians(ug))*radius

    sum_kv=0
    while ug<90:
        sum_kv+=((cos(radians(ug))*radius)**2)*col_bl
        ug+=360/count_bolts
        col_bl=4
    
    if on_bolt:
        P_max = stress_N/count_bolts + (stress_M*c_1)/sum_kv
    else:
        P_max = -stress_N/count_bolts + (stress_M*c_1)/sum_kv
    
    square_bolt_need=(P_max*index_dinamic1*1000*9.81/rasch_sopr)/100
    res=square_bolt_need/square_bolt
    
    return res