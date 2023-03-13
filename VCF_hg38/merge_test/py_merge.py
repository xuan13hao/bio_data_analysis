#!/usr/bin/env python 
# -*- coding: utf-8 -*-  
import vcf
import csv
import pandas as pd
# File path####################################
filename = r'../Fam300_genotypes_VQSR_1.vcf.gz'
csvfilename='../Fam300_2.csv'
#########################
row0=[" ","POS","ID","REF","ALT","Ae0/0","A-o/1","A-1/1","U-0/0","U-0/1","U-1/1","Func.refGene","Gene.refGene","GeneDetail.refGene","ExonicFunc.refGene","AAChange.refGene","snp142","1000g2015aug_all","esp6500si_all","SIFT_score","SIFT_pred","Polyphen2_HDIV_score","Polyphen2_HDIV_pred","Polyphen2_HVAR_score","Polyphen2_HVAR_pred","LRT_score","LRT_pred","MutationTaster_score","MutationTaster_pred","MutationAssessor_score","MutationAssessor_pred","FATHMM_score","FATHMM_pred","PROVEAN_score","PROVEAN_pred","VEST3_score","CADD_raw","CADD_phred","DANN_score","fathmm-MKL_coding_score","fathmm-MKL_coding_pred","MetaSVM_score","MetaSVM_pred","MetaLR_score","MetaLR_pred","integrated_fitCons_score","integrated_confidence_value","GERP++_RS","phyloP7way_vertebrate","phyloP20way_mammalian","phastCons7way_vertebrate","genomicSuperDups"]
#import xlwt
csvfile = file('csv_Fam300.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(row0)
#########################
str1=''
str2=''
str3=''
str4=''
str5=''
str6=''
pos=''
ID=''
ref=''
alt=''
###########################################
'''
FGene = ''
GfGene = ''        
GeneDGene = ''  
ExonicFGene = ''  
AACGene = ''    
snp142  = ''
#1000g2015aug_all =''
esp6500si_all = ''
SIFT_score = ''  
SIFT_pred = ''   
Polyphen2_HDIV_score = ''        
Polyphen2_HDIV_pred = '' 
Polyphen2_HVAR_score = ''        
Polyphen2_HVAR_pred = ''
LRT_score = ''
LRT_pred = ''    
MutationTaster_score = ''
MutationTaster_pred = '' 
MutationAssessor_score = ''      
MutationAssessor_pred = ''       
FATHMM_score = ''        
FATHMM_pred = '' 
PROVEAN_score = ''       
PROVEAN_pred = ''        
VEST3_score = '' 
CADD_raw = ''    
CADD_phred = ''  
DANN_score = ''  
#fathmm-MKL_coding_score = ''     
#fathmm-MKL_coding_pred = ''      
MetaSVM_score = ''       
MetaSVM_pred = ''        
MetaLR_score = ''        
MetaLR_pred = '' 
integrated_fitCons_score = ''    
integrated_confidence_value = '' 
#GERP++_RS = ''   
phyloP7way_vertebrate = ''       
phyloP20way_mammalian = ''       
phastCons7way_vertebrate = ''    
genomicSuperDups = ''
'''
flag = 0
##########################################i
vcf_reader = vcf.Reader(filename=filename)
with open(csvfilename,'rb') as cf:
    f_csv=csv.reader(cf)
    headers=next(f_csv)
    for record in vcf_reader: 
            a00=0
            a01=0
            a11=0
            u00=0
            u01=0
            u11=0
            new=record.CHROM
            if record.samples[0]['GT'] in '0/0' or record.samples[0]['GT'] in './.':
                a00 = a00 + 1
            if record.samples[0]['GT'] in '0/1':
                a01 = a01 + 1
            if record.samples[0]['GT'] in '1/1':
                a11 = a11 + 1
            if record.samples[1]['GT'] in '0/0' or record.samples[1]['GT'] in './.':
                a00 = a00 + 1
            if record.samples[1]['GT'] in '0/1':
                a01 = a01 + 1
            if record.samples[1]['GT'] in '1/1':
                a11 = a11 + 1
            if record.samples[2]['GT'] in '0/0' or record.samples[2]['GT'] in './.':
                u00 = u00 + 1
            if record.samples[2]['GT'] in '0/1':
                u01 = u01 + 1
            if record.samples[2]['GT'] in '1/1':
                u11 = u11 + 1
            if record.samples[3]['GT'] in '0/0' or record.samples[3]['GT'] in './.':
                u00 = u00 + 1
            if record.samples[3]['GT'] in '0/1':
                u01 = u01 + 1
            if record.samples[3]['GT'] in '1/1':
                u11 = u11 + 1
            if record.samples[4]['GT'] in '0/0' or record.samples[4]['GT'] in './.':
                a00 = a00 + 1
            if record.samples[4]['GT'] in '0/1':
                a01 = a01 + 1
            if record.samples[4]['GT'] in '1/1':
                a11 = a11 + 1
            if record.samples[5]['GT'] in '0/0' or record.samples[5]['GT'] in './.':
                a00 = a00 + 1
            if record.samples[5]['GT'] in '0/1':
                a01 = a01 + 1
            if record.samples[5]['GT'] in '1/1':
                a11 = a11 + 1
            if record.samples[6]['GT'] in '0/0' or record.samples[6]['GT'] in './.':
                a00 = a00 + 1
            if record.samples[6]['GT'] in '0/1':
                a01 = a01 + 1
            if record.samples[6]['GT'] in '1/1':
                a11 = a11 + 1
            str1=str(a00)
            str2=str(a01)
            str3=str(a11)
            str4=str(u00)
            str5=str(u01)
            str6=str(u11)
            pos=record.POS
            ID=record.ID
            ref=record.REF
            alt=record.ALT
            list1=[]
            while 1:
                '''
                headers=f_csv.next()
                print headers
                '''
                for row1 in headers:
                    list1.append(row1)
                if str(list1[1]) == str(pos):
                    print 'Match',pos,list1[1]
                    headers=f_csv.next()
                    print flag
                else:
                    print pos,list1[1]
                    break
   #         writer.writerow([new,pos,ID,ref,alt,str1,str2,str3,str4,str5,str6,FGene,GfGene,GeneDGene,ExonicFGene,AACGene,snp142,aug,esp6500si_all,SIFT_score,SIFT_pred,Polyphen2_HDIV_score,Polyphen2_HVAR_pred,LRT_score,LRT_pred,MutationTaster_score,MutationTaster_pred,MutationAssessor_score,MutationAssessor_pred,FATHMM_score,FATHMM_pred,VEST3_score,CADD_raw,CADD_phred,DANN_score,fathmmscore,fathmmpred,MetaSVM_score,MetaSVM_pred,MetaLR_score,MetaLR_pred,integrated_fitCons_score,integrated_confidence_value,grs,phyloP7way_vertebrate,phyloP20way_mammalian,phastCons7way_vertebrate,genomicSuperDups])
