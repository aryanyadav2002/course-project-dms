from django.shortcuts import render
import os
from .forms import Dgbbip
from .models import *
from decimal import *


diaa=1
rpmm=1
rloadd=1
aloadd=1
lfactorr=1
elifee=1
ansvs={}

# Create your views here.
def index(request):
    return render(request, 'homedms.html')

def dgbbip(request):
    
    global  diaa,rpmm,rloadd,aloadd,lfactorr,elifee,dynamicC2,gdynamicC,item1,faByStaticC,faByFr,xyval,mlRevL10,gx,gy,pe,ansvs
    if request.method== 'POST':
        fm= Dgbbip(request.POST)
        if fm.is_valid():
            diaa= int(fm.cleaned_data['dia'])
            rpmm= fm.cleaned_data['rpm']
            rloadd= fm.cleaned_data['rload']
            aloadd= fm.cleaned_data['aload']
            lfactorr= fm.cleaned_data['lfactor']
            elifee=fm.cleaned_data['elife']
            reg=Userip(dia=diaa,rpm=rpmm,rload=rloadd,aload=aloadd,lfactor=lfactorr,elife=elifee)
            reg.save()
            fm= Dgbbip()
            
    else:
        fm= Dgbbip()
    
    
    #item = series60.objects.all()
    #print('return', item)
    #print('sql query:',item.query)

    item1=series60.objects.raw('SELECT "dmsapp_series60"."skfNo" as skfNo, "dmsapp_series60"."dia", "dmsapp_series60"."d1min", "dmsapp_series60"."dcap", "dmsapp_series60"."d2min","dmsapp_series60"."bB", "dmsapp_series60"."rR", "dmsapp_series60"."rR1", "dmsapp_series60"."staticC", "dmsapp_series60"."dynamicC", "dmsapp_series60"."maxSpeed" FROM "dmsapp_series60" WHERE "dmsapp_series60"."dia" >= (SELECT "dmsapp_Userip"."dia" FROM "dmsapp_Userip" ORDER BY "dmsapp_Userip"."id" DESC LIMIT 1)')[0]
    gstaticC=item1.staticC
    gdynamicC=item1.dynamicC
    faByStaticC=round(aloadd / gstaticC,3)
    print("***********************************************")
    print(faByStaticC)
    faByFr=round( aloadd / rloadd,3)
    #print(faByFr)
    faco = (faByStaticC,)
    item2=Eqbload.objects.raw('SELECT "dmsapp_eqbload"."faco", "dmsapp_eqbload"."e", "dmsapp_eqbload"."lx", "dmsapp_eqbload"."ly", "dmsapp_eqbload"."gx", "dmsapp_eqbload"."gy" FROM "dmsapp_eqbload" WHERE "dmsapp_eqbload"."faco" >= %f' %faco)[0]
    print("***********************************************")
    e=item2.e
    print(e)
    # item = Eqbload.objects.all()
    # print('return', item)
    # print('sql query:',item.query)
    if faByFr > e:
        xyval=' Fa/Fr is greater than e'
        #print("inside if")
        gx=item2.gx
        gy=item2.gy
        #print(e,gx,gy)
    else:
        xyval=' Fa/Fr is less or equal to e'
        gx=item2.lx
        gy=item2.ly
    pe=round((gx* rloadd+ gy* aloadd)* lfactorr,2)
    print('/////*********//**********////',type(pe))
        #print(pe)
    mlRevL10=Decimal((elifee*60* rpmm) / 1000000)
    #print(mlRevL10)
    print('/////*********//**********////',type(mlRevL10))
    onethird=Decimal(1/3)
    dynamicC2=round(round(pow(mlRevL10,onethird),2) * pe,2)
    #print(dynamicC2)
    if dynamicC2 <= gdynamicC:
        ansvs={
            'op': 'YOUR BEARING OF BASIC DESIGN NO: (SKF)',
                        'skfr': 'SKF',
                        'skf': item1.skfNo,
                        'dr': 'd (mm)',
                        'd': item1.dia,
                        'd1r': 'D1 Min. (mm)',
                        'D1': item1.d1min,
                        'drr': 'D (mm)',
                        'D': item1.dcap,
                        'd2r': 'D2 Min. (mm)',
                        'D2': item1.d2min,
                        'br': 'B (mm)',
                        'B': item1.bB,
                        'rr': 'r (mm)',
                        'r': item1.rR,
                        'r1r': 'r1 (mm)',
                        'r1': item1.rR1,
                        'cor': 'Static Co (N)',
                        'co': item1.staticC,
                        'cr':'Dynamic C (N)',
                        'c': item1.dynamicC,
                        'spr': 'Max. Speed (rpm)',
                        'sp': item1.maxSpeed,
                        't1':'Selection od radial and thrust factors:',
                        'fbc': 'Fa/Co',
                        'fbca': faByStaticC ,
                        'fafr': 'Fa/Fr   taking V=1',
                        'fafra': faByFr ,
                        'echk': xyval,
                        'xx': 'X',
                        'xxa': gx,
                        'yy': 'Y',
                        'yya': gy,
                        't2': 'Equivalent Dynamic Load:',
                        'pes': 'Pe in N',
                        'pea': pe,
                        't3': 'Using load life relationship,',
                        'l10': 'L10 in mRev',
                        'l10a': mlRevL10 ,
                        'cd': 'Dynamic C in N',
                        'cda': dynamicC2 ,
                        'cal': 'Calculation:',

                        
                        
        }
    else:
        
        item1=series62.objects.raw('SELECT "dmsapp_series62"."skfNo"  as skfNo, "dmsapp_series62"."dia", "dmsapp_series62"."d1min", "dmsapp_series62"."dcap", "dmsapp_series62"."d2min","dmsapp_series62"."bB", "dmsapp_series62"."rR", "dmsapp_series62"."rR1", "dmsapp_series62"."staticC", "dmsapp_series62"."dynamicC", "dmsapp_series62"."maxSpeed" FROM "dmsapp_series62" WHERE "dmsapp_series62"."dia" >= (SELECT "dmsapp_Userip"."dia" FROM "dmsapp_Userip" ORDER BY "dmsapp_Userip"."id" DESC LIMIT 1)')[0]
        gstaticC=item1.staticC
        gdynamicC=item1.dynamicC
        faByStaticC=round(aloadd / gstaticC,3)
        print("***********************************************")
        print(faByStaticC)
        faByFr=round( aloadd / rloadd,3)
        #print(faByFr)
        faco = (faByStaticC,)
        item2=Eqbload.objects.raw('SELECT "dmsapp_eqbload"."faco", "dmsapp_eqbload"."e", "dmsapp_eqbload"."lx", "dmsapp_eqbload"."ly", "dmsapp_eqbload"."gx", "dmsapp_eqbload"."gy" FROM "dmsapp_eqbload" WHERE "dmsapp_eqbload"."faco" >= %f' %faco)[0]
        print("***********************************************")
        e=item2.e
        print(e)
        # item = Eqbload.objects.all()
        # print('return', item)
        # print('sql query:',item.query)
        if faByFr > e:
            xyval=' Fa/Fr is greater than e'
            #print("inside if")
            gx=item2.gx
            gy=item2.gy
            #print(e,gx,gy)
        else:
            xyval=' Fa/Fr is less or equal to e'
            gx=item2.lx
            gy=item2.ly
        pe=round((gx* rloadd+ gy* aloadd)* lfactorr,2)
        print('/////*********//**********////',type(pe))
            #print(pe)
        mlRevL10=Decimal((elifee*60* rpmm) / 1000000)
        #print(mlRevL10)
        print('/////*********//**********////',type(mlRevL10))
        onethird=Decimal(1/3)
        dynamicC2=round(round(pow(mlRevL10,onethird),2) * pe,2)
        #print(dynamicC2)
        if dynamicC2 <= gdynamicC:
            ansvs={
                'op': 'YOUR BEARING OF BASIC DESIGN NO: (SKF)',
                            'skfr': 'SKF',
                            'skf': item1.skfNo,
                            'dr': 'd (mm)',
                            'd': item1.dia,
                            'd1r': 'D1 Min. (mm)',
                            'D1': item1.d1min,
                            'drr': 'D (mm)',
                            'D': item1.dcap,
                            'd2r': 'D2 Min. (mm)',
                            'D2': item1.d2min,
                            'br': 'B (mm)',
                            'B': item1.bB,
                            'rr': 'r (mm)',
                            'r': item1.rR,
                            'r1r': 'r1 (mm)',
                            'r1': item1.rR1,
                            'cor': 'Static Co (N)',
                            'co': item1.staticC,
                            'cr':'Dynamic C (N)',
                            'c': item1.dynamicC,
                            'spr': 'Max. Speed (rpm)',
                            'sp': item1.maxSpeed,
                            't1':'Selection od radial and thrust factors:',
                            'fbc': 'Fa/Co',
                            'fbca': faByStaticC ,
                            'fafr': 'Fa/Fr   taking V=1',
                            'fafra': faByFr ,
                            'echk': xyval,
                            'xx': 'X',
                            'xxa': gx,
                            'yy': 'Y',
                            'yya': gy,
                            't2': 'Equivalent Dynamic Load:',
                            'pes': 'Pe in N',
                            'pea': pe,
                            't3': 'Using load life relationship,',
                            'l10': 'L10 in mRev',
                            'l10a': mlRevL10 ,
                            'cd': 'Dynamic C in N',
                            'cda': dynamicC2 ,
                            'cal': 'Calculation:',

                            
                            
            }
        else:
                    
            item1=series63.objects.raw('SELECT "dmsapp_series63"."skfNo"  as skfNo, "dmsapp_series63"."dia", "dmsapp_series63"."d1min", "dmsapp_series63"."dcap", "dmsapp_series63"."d2min","dmsapp_series63"."bB", "dmsapp_series63"."rR", "dmsapp_series63"."rR1", "dmsapp_series63"."staticC", "dmsapp_series63"."dynamicC", "dmsapp_series63"."maxSpeed" FROM "dmsapp_series63" WHERE "dmsapp_series63"."dia" >= (SELECT "dmsapp_Userip"."dia" FROM "dmsapp_Userip" ORDER BY "dmsapp_Userip"."id" DESC LIMIT 1)')[0]
            gstaticC=item1.staticC
            gdynamicC=item1.dynamicC
            faByStaticC=round(aloadd / gstaticC,3)
            print("***********************************************")
            print(faByStaticC)
            faByFr=round( aloadd / rloadd,3)
            #print(faByFr)
            faco = (faByStaticC,)
            item2=Eqbload.objects.raw('SELECT "dmsapp_eqbload"."faco", "dmsapp_eqbload"."e", "dmsapp_eqbload"."lx", "dmsapp_eqbload"."ly", "dmsapp_eqbload"."gx", "dmsapp_eqbload"."gy" FROM "dmsapp_eqbload" WHERE "dmsapp_eqbload"."faco" >= %f' %faco)[0]
            print("***********************************************")
            e=item2.e
            print(e)
            # item = Eqbload.objects.all()
            # print('return', item)
            # print('sql query:',item.query)
            if faByFr > e:
                xyval=' Fa/Fr is greater than e'
                #print("inside if")
                gx=item2.gx
                gy=item2.gy
                #print(e,gx,gy)
            else:
                xyval=' Fa/Fr is less or equal to e'
                gx=item2.lx
                gy=item2.ly
            pe=round((gx* rloadd+ gy* aloadd)* lfactorr,2)
            print('/////*********//**********////',type(pe))
                #print(pe)
            mlRevL10=Decimal((elifee*60* rpmm) / 1000000)
            #print(mlRevL10)
            print('/////*********//**********////',type(mlRevL10))
            onethird=Decimal(1/3)
            dynamicC2=round(round(pow(mlRevL10,onethird),2) * pe,2)
            #print(dynamicC2)
            if dynamicC2 <= gdynamicC:
                ansvs={
                    'op': 'YOUR BEARING OF BASIC DESIGN NO: (SKF)',
                                'skfr': 'SKF',
                                'skf': item1.skfNo,
                                'dr': 'd (mm)',
                                'd': item1.dia,
                                'd1r': 'D1 Min. (mm)',
                                'D1': item1.d1min,
                                'drr': 'D (mm)',
                                'D': item1.dcap,
                                'd2r': 'D2 Min. (mm)',
                                'D2': item1.d2min,
                                'br': 'B (mm)',
                                'B': item1.bB,
                                'rr': 'r (mm)',
                                'r': item1.rR,
                                'r1r': 'r1 (mm)',
                                'r1': item1.rR1,
                                'cor': 'Static Co (N)',
                                'co': item1.staticC,
                                'cr':'Dynamic C (N)',
                                'c': item1.dynamicC,
                                'spr': 'Max. Speed (rpm)',
                                'sp': item1.maxSpeed,
                                't1':'Selection od radial and thrust factors:',
                                'fbc': 'Fa/Co',
                                'fbca': faByStaticC ,
                                'fafr': 'Fa/Fr   taking V=1',
                                'fafra': faByFr ,
                                'echk': xyval,
                                'xx': 'X',
                                'xxa': gx,
                                'yy': 'Y',
                                'yya': gy,
                                't2': 'Equivalent Dynamic Load:',
                                'pes': 'Pe in N',
                                'pea': pe,
                                't3': 'Using load life relationship,',
                                'l10': 'L10 in mRev',
                                'l10a': mlRevL10 ,
                                'cd': 'Dynamic C in N',
                                'cda': dynamicC2 ,
                                'cal': 'Calculation:',

                                
                                
                }
            else:
                            
                item1=series64.objects.raw('SELECT "dmsapp_series64"."skfNo" as skfNo, "dmsapp_series64"."dia", "dmsapp_series64"."d1min", "dmsapp_series64"."dcap", "dmsapp_series64"."d2min","dmsapp_series64"."bB", "dmsapp_series64"."rR", "dmsapp_series64"."rR1", "dmsapp_series64"."staticC", "dmsapp_series64"."dynamicC", "dmsapp_series64"."maxSpeed" FROM "dmsapp_series64" WHERE "dmsapp_series64"."dia" >= (SELECT "dmsapp_Userip"."dia" FROM "dmsapp_Userip" ORDER BY "dmsapp_Userip"."id" DESC LIMIT 1)')[0]
                gstaticC=item1.staticC
                gdynamicC=item1.dynamicC
                faByStaticC=round(aloadd / gstaticC,3)
                print("***********************************************")
                print(faByStaticC)
                faByFr=round( aloadd / rloadd,3)
                #print(faByFr)
                faco = (faByStaticC,)
                item2=Eqbload.objects.raw('SELECT "dmsapp_eqbload"."faco", "dmsapp_eqbload"."e", "dmsapp_eqbload"."lx", "dmsapp_eqbload"."ly", "dmsapp_eqbload"."gx", "dmsapp_eqbload"."gy" FROM "dmsapp_eqbload" WHERE "dmsapp_eqbload"."faco" >= %f' %faco)[0]
                print("***********************************************")
                e=item2.e
                print(e)
                # item = Eqbload.objects.all()
                # print('return', item)
                # print('sql query:',item.query)
                if faByFr > e:
                    xyval=' Fa/Fr is greater than e'
                    #print("inside if")
                    gx=item2.gx
                    gy=item2.gy
                    #print(e,gx,gy)
                else:
                    xyval=' Fa/Fr is less or equal to e'
                    gx=item2.lx
                    gy=item2.ly
                pe=round((gx* rloadd+ gy* aloadd)* lfactorr,2)
                print('/////*********//**********////',type(pe))
                    #print(pe)
                mlRevL10=Decimal((elifee*60* rpmm) / 1000000)
                #print(mlRevL10)
                print('/////*********//**********////',type(mlRevL10))
                onethird=Decimal(1/3)
                dynamicC2=round(round(pow(mlRevL10,onethird),2) * pe,2)
                #print(dynamicC2)
                if dynamicC2 <= gdynamicC:
                    ansvs={
                        'op': 'YOUR BEARING OF BASIC DESIGN NO: (SKF)',
                                    'skfr': 'SKF',
                                    'skf': item1.skfNo,
                                    'dr': 'd (mm)',
                                    'd': item1.dia,
                                    'd1r': 'D1 Min. (mm)',
                                    'D1': item1.d1min,
                                    'drr': 'D (mm)',
                                    'D': item1.dcap,
                                    'd2r': 'D2 Min. (mm)',
                                    'D2': item1.d2min,
                                    'br': 'B (mm)',
                                    'B': item1.bB,
                                    'rr': 'r (mm)',
                                    'r': item1.rR,
                                    'r1r': 'r1 (mm)',
                                    'r1': item1.rR1,
                                    'cor': 'Static Co (N)',
                                    'co': item1.staticC,
                                    'cr':'Dynamic C (N)',
                                    'c': item1.dynamicC,
                                    'spr': 'Max. Speed (rpm)',
                                    'sp': item1.maxSpeed,
                                    't1':'Selection od radial and thrust factors:',
                                    'fbc': 'Fa/Co',
                                    'fbca': faByStaticC ,
                                    'fafr': 'Fa/Fr   taking V=1',
                                    'fafra': faByFr ,
                                    'echk': xyval,
                                    'xx': 'X',
                                    'xxa': gx,
                                    'yy': 'Y',
                                    'yya': gy,
                                    't2': 'Equivalent Dynamic Load:',
                                    'pes': 'Pe in N',
                                    'pea': pe,
                                    't3': 'Using load life relationship,',
                                    'l10': 'L10 in mRev',
                                    'l10a': mlRevL10 ,
                                    'cd': 'Dynamic C in N',
                                    'cda': dynamicC2 ,
                                    'cal': 'Calculation:',

                                    
                                    
                    }  
                else:
                        ansvs={
                            'skf': "all conditions failed."
                        }        
                

    
    return render(request, 'dgbbip.html',{'form': fm})

def dgbbop(request):
    dgbbip(request)
    return render(request, 'dgbbop.html',{'ansvs' : ansvs})

import pdfkit
from django.http import HttpResponse
from django.template import loader

def pdf(request):
    dgbbop(request)
    #changed after deploying
    path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    #changed after deploying
    projectUrl = request.get_host() + '/dgbbop'
    pdf = pdfkit.from_url(projectUrl, False)
    # pdf = pdfkit.from_file('dgbbop.html', 'out.pdf')
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="result.pdf"'

    return response
