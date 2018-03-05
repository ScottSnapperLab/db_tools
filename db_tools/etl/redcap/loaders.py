#!/usr/bin/env python
"""Provide code to organize the validation and recoding of redcap db dumps."""

dob = Column(
             name='dob',
             dtype=(str, type(None)),
             unique=False,
             validators=[date_format],
             recoders= [rcdcmn.nan_to_none])

date_registry = Column(
                       name= 'visitdate',
                       dtype=(str, type(None)),
                       unique=False,
                       validators=[date_format],
                       recoders= [rcdcmn.nan_to_none])

#date_registration = Column(
#             #name='???',
#           # dtype=(str, type(None)),
#             #unique=False,
#            # validators=[date_format],
#             #recoders= [rcdcmn.nan_to_none])

#date_br = Column(
#             name='Date of Visit',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

date_visit = Column(
                    name='visitdate1',
                    dtype=(str, type(None)),
                    unique=False,
                    validators=[date_format],
                    recoders= [rcdcmn.nan_to_none])

#date_sample = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

date_ibd_onset = Column(
                        name='onsetdt',
                        dtype=(str, type(None)),
                        unique=False,
                        validators=[date_format],
                        recoders= [rcdcmn.nan_to_none])

ibd_dx_date_initial = Column(
                             name='ibddiag1',
                             dtype=(str, type(None)),
                             unique=False,
                             validators=[date_format],
                             recoders= [rcdcmn.nan_to_none])

date_us_arrival = Column(
                         name='dateofarrival',
                         dtype=(str, type(None)),
                         unique=False,
                         validators=[date_format],
                         recoders= [rcdcmn.nan_to_none])

weight_new_date = Column(
                         name='wtdiagdt',
                         dtype=(str, type(None)),
                         unique=False,
                         validators=[date_format],
                         recoders= [rcdcmn.nan_to_none])

height_new_date = Column(
                         name='htdiagdt',
                         dtype=(str, type(None)),
                         unique=False,
                         validators=[date_format],
                         recoders= [rcdcmn.nan_to_none])

weight_prev_date = Column(
                          name='prevwtdiagdt',
                          dtype=(str, type(None)),
                          unique=False,
                          validators=[date_format],
                          recoders= [rcdcmn.nan_to_none])

height_prev_date = Column(
                          name='prevhtdiagdt',
                          dtype=(str, type(None)),
                          unique=False,
                          validators=[date_format],
                          recoders= [rcdcmn.nan_to_none])

#lss_scopedate = Column(
#    name='???',
#    dtype=(str, type(None)),
#    unique=False,
#    validators=[date_format],
#    recoders= [rcdcmn.nan_to_none])

date_pcdai = Column(
                    name='pcdaidoa',
                    dtype=(str, type(None)),
                    unique=False,
                    validators=[date_format],
                    recoders= [rcdcmn.nan_to_none])

date_hbi = Column(
                  name='hbaidoa',
                  dtype=(str, type(None)),
                  unique=False,
                  validators=[date_format],
                  recoders= [rcdcmn.nan_to_none])

date_pucai = Column(
                    name='pucaidoa',
                    dtype=(str, type(None)),
                    unique=False,
                    validators=[date_format],
                    recoders= [rcdcmn.nan_to_none])

#mesalamine_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#mesalamine_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#balsalazide_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#balsalazide_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#sulfasa_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#sulfasa_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#olsalazine_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#olsalazine_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#amoxicilin_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#amoxicilin_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#ciproflox_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#ciproflox_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#metronidazole_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#metronidazole_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#rifaximin_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#rifaximin_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#bactrim_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#bactrim_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#bactrim_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#bactrim_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#vancomycin_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#vancomycin_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#budesonide_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#budesonide_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#rectal_steroid_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#rectal_steroid_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#iv_steroid_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#iv_steroid_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#oral_steroid_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#oral_steroid_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#sixmp_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#sixmp_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#azathioprine_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#azathioprine_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#methotrexate_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#methotrexate_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#thalidomide_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#thalidomide_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#lenalidomide_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#lenalidomide_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#infliximab_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#infliximab_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#adalimumab_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#adalimumab_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#certolizumab_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#certolizumab_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#golimumab_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#golimumab_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#natalizumab_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#natalizumab_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#ustekinumab_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#ustekinumab_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#vedolizumamb_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#vedolizumamb_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#tocilizumamb_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#tociluzumamb_end= Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#anakinra_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#anakinra_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#cyclosporine_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#cyclosporine_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#fk506_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#fk506_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#urosdiol_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#urosdiol_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#cholestyr_start = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

#cholestyr_end = Column(
#             name='???',
#             dtype=(str, type(None)),
#             unique=False,
#             validators=[date_format],
#             recoders= [rcdcmn.nan_to_none])

lab_reference = Column(
                       name='lab_reference',
                       dtype=(str, type(None)),
                       unique=False,
                       validators=[date_format],
                       recoders= [rcdcmn.nan_to_none])

date_labs = Column(
                   name='date_labs',
                   dtype=(str, type(None)),
                   unique=False,
                   validators=[date_format],
                   recoders= [rcdcmn.nan_to_none])

surg_a = Column(
                name='surg_a',
                dtype=(str, type(None)),
                unique=False,
                validators=[date_format],
                recoders= [rcdcmn.nan_to_none])

wbc = Column(
             name='wbc',
             dtype=(str, type(None)),
             unique=False,
             validators=[valid_float],
             recoders= [rcdcmn.nan_to_none])

plt = Column(
             name='plt',
             dtype=(str, type(None)),
             unique=False,
             validators=[valid_float],
             recoders= [rcdcmn.nan_to_none])

hemoglobin = Column(
                    name='hemoglobin',
                    dtype=(str, type(None)),
                    unique=False,
                    validators=[valid_float],
                    recoders= [rcdcmn.nan_to_none])

hct = Column(
             name='hct',
             dtype=(str, type(None)),
             unique=False,
             validators=[valid_float],
             recoders= [rcdcmn.nan_to_none])

ggt = Column(
             name='ggt',
             dtype=(str, type(None)),
             unique=False,
             validators=[valid_float],
             recoders= [rcdcmn.nan_to_none])

esr = Column(
             name='esr',
             dtype=(str, type(None)),
             unique=False,
             validators=[valid_float],
             recoders= [rcdcmn.nan_to_none])

crp = Column(
             name='crp',
             dtype=(str, type(None)),
             unique=False,
             validators=[valid_float],
             recoders= [rcdcmn.nan_to_none])

creatine = Column(
                  name='creatine',
                  dtype=(str, type(None)),
                  unique=False,
                  validators=[valid_float],
                  recoders= [rcdcmn.nan_to_none])

bun = Column(
             name='bun',
             dtype=(str, type(None)),
             unique=False,
             validators=[valid_float],
             recoders= [rcdcmn.nan_to_none])

alk = Column(
             name='alk',
             dtype=(str, type(None)),
             unique=False,
             validators=[valid_float],
             recoders= [rcdcmn.nan_to_none])

alb = Column(
             name='alb',
             dtype=(str, type(None)),
             unique=False,
             validators=[valid_float],
             recoders= [rcdcmn.nan_to_none])

pucai_score = Column(
                     name='pucaiscore',
                     dtype=(str, type(None)),
                     unique=False,
                     validators=[valid_float],
                     recoders= [rcdcmn.nan_to_none])

hbi_liquid_stools = Column(
                           name='hbaistoolnum',
                           dtype=(str, type(None)),
                           unique=False,
                           validators=[valid_float],
                           recoders= [rcdcmn.nan_to_none])


pcdai_score = Column(
                     name='pcdaiscore',
                     dtype=(str, type(None)),
                     unique=False,
                     validators=[valid_float],
                     recoders= [rcdcmn.nan_to_none])

#steroid_priormo = Column(
#              name='If yes, how many months was the longest course?',
#              dtype=(str, type(None)),
#              unique=False,
#              validators=[valid_float],
#              recoders= [rcdcmn.nan_to_none])

#antibiotics_priormo = Column(
#              name='If yes, how many months was the longest course?',
#              dtype=(str, type(None)),
#              unique=False,
#              validators=[valid_float],
#              recoders= [rcdcmn.nan_to_none])

