import base64
exec(base64.b64decode('aW1wb3J0IG1hcnNoYWwsemxpYixiYXNlNjQKZXhlYyhtYXJzaGFsLmxvYWRzKHpsaWIuZGVjb21wcmVzcyhiYXNlNjQuYjMyZGVjb2RlKCJQQ09FTEcyWlNPVkVCTjVHNjczWjNVN0Q1N1VJV0U0UkM1RlVSQldNUkRYSTRWU1JLRklWRVJLQjVaU0VRRUlGQUVRUlMzWDNRNTM2UERYSVVHUklWM05PS0pFRk5MWFZYM0hWV1E3NDQ3NzNaN01MN1Q0Qjc0WERXNklJT1JGNjc3UjQ3WjZQVDdZUDZQUDZZNlA3QUg3NzY3WVQ3NzRFNzc2Skg3WERKNzdDNjc2U1A3N01UNzdWSjdaTTZQNzc2TVBYN1g3Rks3NzdLS1FQUzU3N1c2NTYyNzdaRTM2SFQ2VDc3Nk1UNTNESEs0Q1ZRVkEzRUFOSEpHWUZXNVhNVkNXNVZaUDVEWk9NNVM1VFBGRUpZUTVBMzJWSFBOVzNIRlJaUjNSVU42UTNVQlpOUFRIVUM3RlM2S0hQWTJISjZYM1ZaSFpWV1BGUlNKNVhMTTJUSEVTMkJDSjRDTkRFQ05JTVVFU0FGUlNBWlRGQVVVQURSQ01CQU5YSTdPQVpPTDRYN1lSS1RCUVhINlNSSUQ1QTZBSjJBUU9MU1hBREtGWTJZQUNCNkpGSTNLTTNVQkpUNENDS0pTTzc1SUNDQUlWQUFXVUsyNTJPRkNBNlhGR1FPUUdYUUpJSU9CWlhHUFdPSlNaUkE0S0RDQUpDSUVKNkY0WDJBTUM3SEk3TDNRVExRSjVZR1k3SElVNlNPWjVJV1FPVlg3NUNSVjZXNllVU0lMWUZZVkJOMldGSTJUUlo3R1ZFWEFXTlREVkdNS1VBMlVaSE5aR0NQNE9SMkxKVkpPUjJVRUk1TkVMS1JJVE1KTEVaQllUWkxUWlVGNUVJSEZVVUxNWUhLVktQWEJOQk1EMjI2SkpJSFJBTUxSUlVSTzVZVEtTVFlMWVpYQUVUTUlQRkdSS05ZVFBDSjJOVVRSTk5JSU1FRUNGTFFUSjNKVU1WSkU2WlhWVkdJWlM0UlpQTjUzR1dHREVVVkEyNEU0U0JQMktaTkk1Uk5MUlVRMzZNRVlLMkdZU05ERFUyM1I0UFFEUU5LQ0o0M1pKRTRESDZZRVNXQTIzMlZNNU5QNkFPNEhYQVlLVjU0NlpPVlFER1lSVlhKUDNNR01LVUdaRlNERUZLMk1ORUFKUFFTQzdVTkFBWllDWFZKSjc0T0dKV05CT09MNFJZVEZRUUpLTzZBN0JORzJOM1RZRUNQVFA1R0NCTTVCTEZPWUdYQllNNjVIRlU0RVVFR1U3S1JYSkVMTVZRNkVVVFVaWEtZV0RLNUpHQVJXRlBZRUQyRktHWEtERldYN1FCSlFaVllFQ1NMMlJVVFhaUUdMU0RaSE5LREdCSlJJRjJSUkZJMkI0WUUyNU5CS0lDVVpFWURMN0RDSTVBR0gzQTRJR1pRTU1KQ1JUUVpPU1FHMkEyMlUyQk9IWUJBRTVJWE5LTUc2TEVXTUk0VzdJUUJEWVlWRjM3VDdIN0YyRTZZRjVJVVdGRUNUSENWRExQTkRFTUtKQ1dMV1Y2S0tPWU9TRERLSU00TFVSRFhXS0czVUdPSU5YUk1NVVVaVTY1U1ZES1lLUUZCWUlSSFU2NUY3WlJJT1AyUkFHVlJCUkFUN1ZDUUtGU0lRQ080RlFONFU3SEdSTUhGRDUyTEE2RjNJRFRSNTRMUEZYNEFQS1FZVEdQV0I1SktZVFJSSVhDSVhLR0hQRUdLM1U2RlFCUVFORDU3VUJZU1BWWVo2V1lOMkZIUlo2SzIzRTdDRVRWSEZMRjNBNUFRRkgySzZWN0VITU40TkVXTkVQRktISkNMNTRIWDRWSlJVNDIyNkJWNEtQNllGNzVTR1FQRlJJN1M1M09JMlVNUUhEUERRN1E1QUVGREFFT0pEQTZOTDVHQlMzUUlNVkdaWlBGWTZHWVVJTDVIRldWNVJOVkdYT0xISU1INDM0Nk5TSVJHNkxQSktHR0FMR1ZVTlE0QlRHWFRIS0lGSE1KWEFKTk1BWlVET0NBTVYyUTUyTkVEQUJES1BNQTVKSklQWDJLS1pVM041N0w2VEFUTERXQ083RVg1U1VKNUZYNlRaSkE0WEVaNVFUU1FMWjRZRk1VMlE1TlVUNEVENk5SVlY0TzZGTlNENktDT1YzVFgyQ0RYTUVNNE8yVURNM0dKQjc2UFlJSEhIUUNGUExERVVTV1BXUlRLTkNYRk5LQjVUVTNTRzNUSlg0S1FMQlc3U1RQSVFWSlNGQjNJU0laTlU1NTNWQjJHU1ZZR1FJNEdENFM3RUgyU1RKUk5aVzZEUlUySzJLSE1BNUpVSEYzT0tNMzRMUjdERFdQRkdES01YWFpTTDZYVzdNRDNKQ0hXWUNMNklTV05LTldYQkNBNFEyTkVVWENSV1RMUUI1QVhHRTdRN09TMzROUFZNN1M0Vkc0NkQyWEdSWldCUlE1S05YWk42RDZaNlRRMlNYVUVFQ1daRUUzNEVPVjdUQjdTS0M1NFE3Wk9EWktLVEo0WFhVSk01UkNaQ0VUTU40UTVWNUhQWUdKWlZSWUZBVzdHMlNUQkM0Sk1NVExSVzdBVFY0QzJCVkdEM1FKNEI0Q0NIR1VNMjVHR1RGUkU0NzJGUVAzQzJLMlRBR0lBRDRVT0JPNU5IM1hJN0VIRVpIUkZGVDI0UFJZVlNKVEtWUzVDNDRYUkhOSzdDQ1hSSVhVTzJMTVJRVk40VUNCUDY3RUtTTlpRSlAyQzZJQTJXU1RQWVJUWkQ0UUZKSlBWNU9NQk5KUlBJQzM2Q0ZORUJHNVJRN0lDTEVHUk1LSzJGNFhDTTVHWVJCWFdFQVdRQkJQN09YVkFOUUVaTFhCUFNGSjRRSlRJQUoyNU9SNkFIUzZSTFRNVDRLUlBJQlFSNDdIREdESTJNTVlBSTVCTkc0TzdGQlVLVlUyVDYyMjJONVNITldMNTZDNFpJVzJEN0QzVUdRVFg0RVNZVTNLWU5TWkRGNFJTSjdWQjNSV0lDUEwzUVZNU0hGTUVDUlRIQ0hUV0xHT1JYSkRSM0pKREVFNEs3UUpSNFM2NDc2SENOTFc3U0syRUVUTFZXM0NUMzNIRkIzUlBZSTZPV082Q05PUkYyUUFNV04yTEVKR1pOVEVWVUgzTk9QQkRNT0ZXT0hEUExXRTJTVlg0VFlaWlUzT1pWUFczRVFQUUVIQlU0WURPNUhCRVlET0w1SEVCWUg1R1EzMjVSTU5BUEtTQ0YyMkJCQzdUVzZIVktMTEg3SDZEQ0NIVjNCNDZJSUFXRkZQNlU0SlVIRlNRUDRWRjNXQldORjZRVlVZQU5QUUxKQ0xURkk3QlRMNlVLNkU3TDJDS1BHRTJSTTdYNzRHT0VRWFFZRE5MWVk0V0hLQk41Mk1YR1VBWFRUVTJCMjNTNlVPVVpLUU5YTVBGU0hPTUhHNVo1S0xIUlY3SUtWSVQ3QjRHSkgySU1HNVZWRTMyU0RYREdLUkg1RzdCWEdGNFFJSFpEVVJaRlJFR1FNTUpMNEVSTU9WUkZISDVHNjZDSlZNRkk0SkFCUFJRNFRXWkRWRTdTN09aNjRXSEJTR0RFS1RQNUg2NjZNN0ZSN0JQVU9QWEZXT1hKNERXWldCNTJYSVlBVDdaVVpQSlBaQkpCWUNWUVlPR0VMM1RYRUNTR0ZDTEMyRVhQVUM0SEZSTzJEUFNGTzVZVEJVVFVPN05KVU5HSlJWV0RVUDNBWVlNWlJZT1lXR0hNVDdVWlRTN01RVlNQTlNCWkhFVE1EVFNTNU9UVFVYM0lERlNDVDMyUkpMS002Mk0yWkpMM05FRTJBTExKM0xTUUhaVFAzVU9LT1ZHNzVQU1BXTFo0U0tRQzNXTTNFUTJORVVMTUhSMjNDNkdERDY0QU1aNElGQ1hXTFhMS1QzWldETElWRk8zUVFOVlI3UkFJV09PUjJSQTdBRFNTN05ZUkdETDZKSkJaSUQ0WDROTDNRR05YRlJZTldIUFhJTERWWVJaVTc2SlNMN1JQWERZU09ETFNSU0xWM0NISjdVR05ZTlVDVEpOQjM0U0dNNERCT0s3MkFSNU5FMzYzTldFT1c1RElURldVSTdHT1pDUlIyNVRMWVZUSUQ1R0lDTlVXU0RTNlBEWkdMWTNSTzVKUVRLRTNNRFlNVDM2RUY0TE1BUVlVTTZONVhYUlVLVEZEN1NKN1dDU05KN0dGR1IzVjVJQTZaS1NMRVlLVlNOM05QMkNQRlhLM1lUV09PSUhMV0lQWkRBS0dCRE9VTDUzUEdFQU1ZQ1hYSjJMSUhCWkoyTTI3QVBJNlRVSEdUTE43N0NWVU41WFFJM1BGQ0g3QzM0QUdaWkJUR05IREtKTkZVNDVKRVpaR09GNDRDV1o0WUJEMkdYRTNWR0dTMlkyUk5PVlhGN1hFSUdWQTVMUk5HNEZTTVVGTlBTSVVHRUNGQkwzV0tHT05GV1ZHQ1NTQTMzU1RQS0laTjRFVkxZWUhGVFo2R0xTRFFMSEtZTUpTWjVMRFZTVlNQQlJYREFaRlNRQVRINVNFQlVDSVlGT0dJWjVUTUo0NUZZRzNEQ1RPNkhYWkRJVURMNTVKU0ozUlgyRVRFRVBTS0ZKNTdHUE1UQ1I0RE80VjRRUktQNlZBTTRYUUIyT1dZWFhGWURETjNaNTZZT1NQVlM0RU1PT1pBSUdZTlhJM1NXQzc1SElGRkpVSU5XTVRPRENIVEJMWE5RUEZIRzVITURaRzRXQ0tPT0ZVSlU0N0VMTVlGU1JQUzdFRlFINUdUU0dFN0NTR1pTR1RNQTJJWk41SVI0UTNXMkxRNkJQTkM2Sk5UN1E0SVUzRlNBV1cyTEw3N05MQVNBSjZWSUQyTlBFUlJYQk1RWDNRRVBJQU1HQUsyQzNUTkM2SjNaNU02UUJYV0RUTENQSzZRWDdPQzZIVkFTVldBRzVXUkxPUllXTzJGWUxDSkM0SUtFT1dBSjI1SkRQWEVJRUdGM0lCSVlNUVlMSzVPSE1XRFY0Q1JZVExWS0NQNVFNQk5RSUc1SlNZVDNJSkhURFVXRzJSSjVCUzVMQ0g0SUdYSVdCWEhBMkFPTkFXTU1NSFdIV1gzWlhaMk5XVEJXMk00TFZNT1lJRlZJUlpRU0E1NDVOWDZaNFJGQUJTSUVISk00TVhRT0JOT1NBRkVVREtSM0tSM0kzRVBXUURYREkyUEo3T0Y0UEtIV0lZRURMQVNUQkIyRkVET1hVNVNNNlVDTzVYRlFZRzdCSkRFSzZZTlU1WDJBTzc1SzNNQ05FMkRaR1dIWlBCRVY1REJRWExRN0dGUTJYUEhUTEdBT0w0RUJUNFZQSlAzRFdHNjNKUjVVV0FaMlpBSkw2TkVONU1WNzVUV0xRRERDS0FJTFZYM0dSNVpSQVdSTENaTU5ISDJQUktZT1BPMzc3R0RNWENRT0tKR1RRMlZJNVVXQkhNVDdURldQUklQU05NVERPS0tSSVBIMzdPQ09QRE00SUY0NElMVzI1T1ZKV0hESkFGU0dFM1FZUFBERk1RQlVIVzZPVE1NN1pRUzI2VlFRR1IzNFlCM1RCQjNNSkRVS0lQTkpLQ1pBVk5FVTJLRTNXVUczQ1ZMSlBOUk5WSkU2M0RBNkJZRDVJTkxKTkpFSlNRQUwyTjVUQUhTVUNINkFBV1RBRVBNU0JGU1JYS0pSM0xHUlJCUFdKRURITU5ISkEzR1NGWEpZSFI0NlBJSDNEMlBFNzNKSjJaUkJLSEdBRFozSk1NUFA0MlFYVlREVENUNlJNTEZYN0hOVklGMlNQVFpHMkZTTE42M09aRlpTSE5WTVM0VVZCMjZKNVEzTVFYNUU1U1FKNjNJU0YzR043RUJYVEM3SlhFWDNMQ1U1REw2MklTS0taVERXNFc2TklDRk1GSEJDUU5XVEhNWEROMlVZM1pOWDRSUFVZUEJXTEQ1SUxNUU0zWVlDNzRBVENHUDIyNFVTNkdUU0dBUDVFRjNaNFhNQ1BCV00ySEg1UVlBTzNERDVSWVpKQ1BXMkhNUERJNFcyTlFTUUJHWjQzQkFIQ0k1NTdVVk5GSlczNFBINUdWUVZGNTVJTFhHV0ZPVEZZWUNMV1VNV0RNRFdZUDZKS0gzRTREWllFN1NMSTI1UjI2V1dZWUhVN0gyREZETE1XSEpaSEdOSlFOTlFDQldQU0ZZT1JOQjQ1QlpGNUM0T1RVQTVXUUNWVlhIVU5QVkdRV05BWDcyMlFPTUdONjRFT1dXSE9aRk1MVEJCN1VFR0VCTlBGWE9LRUY0VUpGVks1VDQyQ0lVTjRXNDZUN1czVTVLRkEyTkpNTkFYSEY1NEtQUERCTklLT1Y0SkIzQ0w0RjRTS1RXN001WjNTSUZWUzZBTFBaUFVDUFpEUzNMWldCSUg1VVhQVUxONExOTVpMSTVPSlg2TjM1WUJQS1pQUENVUVVBWFdPTUNGMjdCWUxJS0dURzVEM1g1TU5FTjdJUVVQWE9TMktXRDNYWUZSQlhFRkVMWkIyUDQ0RTVUVFVFNVBTUTNKRkk3TktQRElCMjIzRlNNQlUzNVBNQk9CVjREWUM0WDRRRE5EQzQ2T1RIVlRYM1RZR0s2Sk9ER1hXQzZKMkpFR0dHQTVZTlFNUkNRNkRPN0E3VklWUFI1SUxWVDROR0hPVDNDR0xTTEtLWkhORDUySTIyTEQ2SUtIVUFKTEpNVVhMNUs0QlpVRk5FRTRQWFQ0Uk5aV09PSlBGRU5QUDRZRTNVWlkzT1JVMk9QNlpBWkNFSjNaM1BOVVE2N1IzNUZGNllITktYRkFORU5VSjdISFNIN0NOM0Y0Wk02TkYyVE1EVVFVNTdDV05PRUlLNFNQRElMUFVVWjJHTVg2SEFEWVhTQVZTVU9LM1JHNVRDQ1dRTDZHWVJPRUIyUFFYNUJKV0I3RElRTk1RR043QjdKVlVOUzdNRU1UVlFPUkIzMlNSRFQ2UlNYUFQ0SVlOTjRETllGVzNFM0tIUVpMSUhMSUE3NEJUQ0ZMV1BPTTRIWU0yNkxBSVZKMkhGUEs1NU1NRE5CT0pISjJUVEoyRUpQNzROTVZLVkVHM0ZGVEhZT0daVFI2VEhVTzRMTTRYVEEyU1AzSUxOVkdOTTJMVzZaQ0NaSTZIR0xYMkhCUlZVTjVHVkZLWkhZSFJRVjMySFBNRjM1V0JWNDRDS1hPT0dGN1pMUFU2TEdRNERXUlRRNTNHS1BJWEtSVDJNUFc1QTNWWldDQk9GQUszM1JZUzJPM0RIVkROT0tJSFBPWVJDQ1lYM0hPWTNQUVBRV0dGWE5HRlJHUUlGR09QQUdIVzI2MjNTQTY2VUVZMzJWREJRNU0zNjI0WkI0RENaSlhLRUtJMzdONEpaQ0JSWFhCRUxGNU9KNEdOM0c0RzJDWENMWFNVVVpYM1ZBVEg2M0NVVUhOTzJDSEEyNlpBRVg2RUhLNjNCUzY0TDRFQlNNSkZISk1TR0c1WkVPMzJXT0RLWldGRUYzVk5GNVg2QU9USjU2TENCRzZQUU5KREFCTE01S1hYSFdSM1lHTVZGWkVONlpEM0FZTTJCTjVWQTZPUFlNVllIM0JZRlNISFBEQVRCNVA1TzRXVVJKQjRGVzJVTUtXSU5RSk1FN0NHTzJIR0w3R0pUSFlHTTJKV1FMTkVaVzM1MjRaVzJaM1dTWFVDNDJKQ0xNWE9DVUhWRVdRNllOVEpNV1paTFZSRTdPVFRNMzZXR1BaV0Y3R05OTkZENk1QUTVPUVdKSktWM1AyWVMyVkxPWFQ2UTZUTjZOSU5BTjYzWUlQVkJRWFdaMlM1MjQ3VDZZR0xKVlNZTzZOSUo1QldZUk5VREhTUDZXUkZQTlZRNENNVDJMN1FWQU9CUFlBSE9YQVJNVlg2NkhHUlZOVkQ0WlVEVTZMVTJIRlNHNkxKQjVTTFIzTjcyRUFQWlYzVUlVWUxSTU43NVNCQkZaQzQzRlJKQTdJR1lCV1NaVUJBS0VNVzJTSFU0N1NZTEhRV1g2WVlaQjJPUjJOV0s1S1o3N0RETjZDR1NJRFdNQlJVNVRKREFNNk9SM0RWVEpERVdVWjJRTDJIQjNNR0U2UFJaNlZZS0lLTUVSNTZOTk5PQVk2QkZINDVXUE5KSk9LRkZKRVlPVVdHTEFTUFZTSlVPWjZFRVpSQ1VKR0xHR0MySDRHUkw0NkYyM0laVjVLREQ1T0NOR1VHSlRVV05YWVBNVVJIWlVLRFNDNDJKRjNUSDRHQlVGNlpKRUFHNURKWDVGWE1NT1VUQUxaSjZFTjVOT01PSktMQkRFU1JXTU9XR1VXMkJOSERKUFBXMjU1NFNFTVVIVlFVN09IWjZQRDRNNElRVDczQ01TRU1QTFhHWjRSSjJENVJHS0tJSU82RU9JN0NBSVRKMzNVN0tOUVpMR1pZUlBCTFFYQkNQVElRUFRPVEtTNUxSMllHQkFYNTZEVlNGVExJV1ZHRE80S0xFT1dXQVZBWlpCRzRUNk9ESlZaS0IzRldPSE1TU0pOUkJWSFRTUkdUUjdGNkFNVEtHQ05ISUxTSldKWFJJU1pOTkNaWk0yRTdLWVVBVkFXUkxHUUVLSllTNEhMU0NRWEdKRzI1NEs2SENONlBLWlpFWkNHQjNZQjUyR1RGWlBRN1hNWEZIUUlaMlZUNllKNTdVRlU3QkEzRjZCVk01VVNDWVVZUFdTN1JOM1hYNkY0MkVSNVVaR1hYRDZHS1Y1R1NWRUhWSVlHM1M3QVYyN1FGNFFSTDZQVE5CV1U1U1RLUExZRldRTlk0TEdBNFBKRE5DSktPUDZDRFg1RERITDNLVVNMNUdHVE5ST0pLSUhXUUkzU1VPM1BYSE9NTEQ2M000MkJNS1JFWkVZT0haR09OR1dYUk4yR0taNDdTQlI2WVdIMldTR1dCRUpPSlJDN0VQSlhIMjNLVzM0UDdMS0syNkc3RUk3QzNLR05SN09WTllBUENUNkNLSFBCN1hXSkk2UTM2M0lYTzdTN1JLRDJUWEdTRldKWEdQTVY3T0RINVFIT1U2WklSVU9TRFlSQkVCQ0NUNlc2UkZKN1I2WUhQV0FPTDJWQjZUQVZXTVpINDNWVUFXMzI1VVFESlhEVk1WVENaMjJBMlNYVEVNT0pRWElFSzVLWDdKTUhUUEZLWEJEM0VSTUtBVFJYNkhWWkRMV09aTDM1UFRJMlBLQzdFTlZRTUQzTkxCQVlYNVU0UUZYNEVVNFkyMjIzTFpDNFVMQkpTVVRYM0VINFZXSzRRWlNIRExKQ0JKSkZQTlA0U0NBVERYSEhZQ0s3Nk41QlhKQ000WlA1RFlGUFVDTFkzRVk2QlNONVpQTzJSNzZQSVlVWkdTWENUMlZRWllLNzJJMlNaR0NaSFJMWFZXSkpQTzZJVlE3Q0NLUTVUTlNGQkhMRjRPN1FTT000RVVFVEVZNkxCWVRDUzdZMlRQWUxCMkVVRUdFWEE1TldPWFpSMjJJM1gyM042WDRKVUQyWkhDV1o1TzRCRkc3TzdXQTJMNExNNUJCTFlUR1NTN0hTU09VTUlFTVJGMk1ER0tIMzczTExWRkY2M0RQTDNMSTVXNjVETjJVQzM3QlQzN1RXSkZBUkZOUFZQRUVWV05DTzQ3NlZaU01HWUZEMldaTFk0UENaRDRRWFA1NklNNllOUEZOWlpCQkdHUU5QSjNMRU1IWUZEMkpSN1NZWU9PTVBJS1hBSlpBNFJXTVlERTVTMkY3NlIySUVRR1lZTE1NQlVYUUtDTTMySFFXSE1YVk1WN0tSNTRNQjNTTzVUWkEzVkVEUkZXSDJOMlRPVERISUk2UEMzUklWMjVCM0pQTTdBSE1EWURNUUtQQllaN0FKT1dBQ1VDN1hUSUVPVlJPRjdPRTc3TE9KWDRaWFNYR0wzQ1pVUFVKVVoyRjZVVUYzU1FPNENKQVpWWjZEQjVITUNISE1PWkZINjREUUpDUlNaRFY3REZSVVY3S0tPNUdMNjVBNjdDTEdHQ1kzTFhIQkJQNUZJQ0U1U0pER0s0VkdTNk1ITjNJM0wzR05ZTklVVllNT1hIQkRDVFBETlRINDRFNFM1RTUzT042N0VRUkdYRVBKNDJFNUwyV0E2VUY2RVpKQjRQVlI0VlIzNVdFWldUNVNDUEZUU0tNR1FKN1NRV1NHVzdIR0ZZWkJIR0tYMlpLNk5WWjRXWEwzUVYzT0U3T1RFV0NUUUE0RTRYNE1GUDY0M0IyMkwyTFdPTTNDWjZJVEFVMjNVSFBCRE8yWlBIRlU0TlhZQ0tYRlhKQTVEWkhRRVJNRVdTV0ZGNFFZVDJXSjVMMjJQWEE2MkpWRk83QTJVVjdJUEJYREgzTVVIUDZPNUZVRzRCWldXWDNVVFdFV1lTMk82Vjc3WERDSFdBUDRVV1ZESEgyNVpRVEpOTkRRRVhYWE9WRlg2R0YyM1VaQ1BTVzVENlZNVFJRTVgyTTRMNlRINVNNQzJXSkxPU1RSWENLVEdEWk9BSk1XTVlaNDNIV0FNQTNYSlhHSU1OTkg0UlNMTlJWWFhTWjREWjdGSVY3UUdLU1o1TVVIQldPUkQ1VDRERklQS1dCVU9CN01PVUhKT1NFUlhENk5QVVlZNldOMllSRVc3QU1HWkNDNFo2VTdTVlY0S0JLVEpLM1VRU1hZWVhVM0M3NjZEUzJPWVlHVlNLN1ZDT05HVzVDUE9aRE43R0E0TlZZQkdEUFFSWVQ1NUJIUlZMT0dPVVNKUlBMNEpWQTU3TE5QS0lUUkY2SlhUTUw3TklZSEZHTUNDUjdXVkJHTzRCSU5ESU9CNUhWVkhJWDQ1RlVSWFNPRkFIVlcyTFRJVUlQV0wzNTRDVDYyTlBLRTVFTU9LTUI1RTZCNUQ1NEw1M05NSVFNN1hTTU5HRTRUMjVNWEQzS0s0WDRIV0pQQ1dUWUZXR1BLN0lEN0UzTjcyQ1ZUQjdNVVo1QkxONzROMzUzTVVOUzZPSlZNR0xPUUs3Mk1DVjY1RjVNS0xPT0hFN09FWUQ1QkpRTFgyUlJVMkxGT0lQRVJFWExTRVk0V1pNSUpWWE1OWlJXWFBHVzQ3VEpMUjRFREZENFBFTkFBMzNJMldQTE0zU1NJTlFZNFhYWUdPUVgzTERORlFDTkpYNUFXVzJHTFVFSUM2NUtDQjUzSDNJRTIzUFhWRERBTkZMQ0VKUjNTVUkzVk1WUjZWNEpYN0Q0TzNSVVdKQUlXNjNaVUFSNkJKNENUUE83WkVSNVNGRVk2TU5BS0tCUk5IV0VNUEpBNFA1NjdCSE1UU1U2NFhZTzVXVlVNUDI3R1lNMzJYV0c3UlM0QTRYV0xFUjJTTU42WkFZRko2VlRJVkc2T0FQQlVGWTVHVVRPUk5GV1pGQ0c2SkpKWEo1RUtDTzNRRVZFVFVOQ0hGVzY1VzZBU1FGWFJHTElCN1NLSkJKWTVPS0taTzVST1ZIUDJYRElaNTJLUFhGRzZVWEEzSlQzUVIzVE9CNEFXWE9PV0pHSVI3VFNKVVE1WElLM1RLUVUzQU9BN1JaUUU3QVhINFczTUM3RFA2V1NUUVJLS1ZMREFJREZHSTNETEo1REVUWkJVNktDQ1FNNzJCTjNJWk9GVUdIMk1TNDdCUU5QRU5JUEFWSlcyWFBTWEJOMk5GNUdIWTdUT0Q2UENOQlVKS0ZIUlpEUkJYRUZaUzJXSUVUNkJJV1BNM1BVQkZCS1FYTE9QSEVZUVpYWUVSUEZLRTZDSklaNEpNUE0yVVVPNlhBSTZDSEtMNFpJWEZONDM2SkhDMlhVSUdWM0ZZNE8yWFU0WkZPWjdMSlhNRjJMV0NXUVVYNU1RTE1XN1hLWE0yN1NOMzZJQ0Y2SURQV09KNEZYWlZPSU1GUkQ3WlhNS1lZT0E3Mko1U0FZSEE3M0VQVjJGV1VNTEhXNkhWQU9TUEpBQkMyWEtITE1IVVdVQlpaWUgyU0pXS0pPN1VaRlhWRkE3RTVNRkZKWE1UTkhFQjNOT1BNSUQ1NlhSUFhOUEdMUFZKRFIyNExKQTNBVjJCTFFCTElLU1ZRUFBZVUhPMkoyVDQ0R0ZFSlRVWEhSRlhYNzRJNFBINFNKV05XR0dRN01PRlNYR0NPQVJNTkxDT081M0JEWTQ3UFVaTDVYUVpWWVFJNk1NS0wyRVo3RTNBUjdEVVU2VEJNUjJEVEVDTUVZR1EyRkM3WlBHRDMyNDU3WEpIVVFSNzNVWVVPS0tRWktLTkxKSkNWQ0VQSDNKRTM2UjNERDVQS0dPUU1LWldMUkVYVjZRSk01SldCSUdGRzNISjRHQ1FCTzI3R05OVFdHWlVWS1ZXVkdPRUIzSVBKV1JTNDdFRFFWSFFITVFNWkhSV09IUFlTSVhWN0EyQ0oyQUgzTUJMMkhBWlBESTc1SVdINkUzRlFXVUhIVlFZWEw1UkdGMldOWVVCT1pWNE5aMk1MV0pZNVBHRFZMUE5BSUszTDNJWk9HTTZKVElVRVRPSVhLT0xGMkJGV0VDRUZFSzdEUVBZNkg3Q1MzS0dPQVBLNk1JV0lNTkw1U1JPWkhIT0k1UEM0VFZXSUdSR1FaVVY0SVNUTUNVVlBUUEpDRFdLS1VaTURQUlFTVDNHTkpQSjRFTURNNFRMVlRCWk5UNDc1VU0yVTZUM09WNzZPS0xUSjM0TEFZTFozNlFPMzNKTlVQWk5DQ09OVUNGR1dJQTI3WEdJVUVOVkY0WjU0Vjc2Nk9URjNHN0EzRE5EVE01R1E2M0pZMzU0TkdGRU9SSlhCRTNKS0VERTZFWlY1TVNSSlFJWDNPTFFIR1BDR1lSTFpLS1UzNlVLQlFQVkpIRUNNM09URjNLSlBLTkFOQURTNkxNVVpLV1RHVlRKN09OTjNBRzdPNUVVRE4zSFZFMlQ1V1EyWEpDWUhYRlFZRUpOWUJEU1c1WVRZRExLNEhXVlNQWDVBVjZQNlE1SFIzNkoyUklFM0dHNlVTSERPS0pJTllMSDdBQVc1MzRGNkdEVEZPVDVZMjdTRVpFTlI3VE9GVzVQTlpZWUxTVEJLVlVaWlNSR0JOSjdYWk9HSzMzTkpWU0FYUDZEWFFYSFY1WUZJUDNMUU40SFZFWDRLT0pYSzY3M0xMUFNHNFRHTkgzNUxEUFBBUFJFUVVYQ0JRMjJNV0syNFVYVExDMzRVVjVXRURKWUxCUkZBTExNRVRSN09DWTNKT0RPUFlENVBHNlNDRkxaQ0FXU1JQRDZIVDZTRlFMTE5NS0NYM0VYNk8zSlo2RjVOVEw0UzdKS09OVVY3QllCRllCSFA3QU1TTkM1SE5UR1BKWkM3NUdPNUxUTDM1WkFTQlFXTjI2TTJZQ1MyRkpHUzNXU1NTUkFNVkVQT1g3RUhTRElJUFk1WElPVEwySEJRVERNNlIyWUVISklaV0FaWFNTWkpNVFEySFRKRTMzVUpNQzNSTjdXNE1EQ1lNWE1DVEE0Qjc2TE9VQzVXVVhOSlgzWkpLNlRFWkxIU0NBQk5UTE5FMlVXUzNRU0laWDRZTjdaM1pYVFdRQ1FTQVpWUVpLSE1KNVBFR1YyT01WN1FaUk8yWDNRU1BVRzNUUTY1RE5YR0RZNDdVVU9WU1pYUTJIR0dJVzNKUkdaT0czUFNJMllXU1UyUFU1U1NHN0xQTlNINVlQTElQUTJMWEo1WFZNQlA0VlhHVFpQMlBXUlg3RlZBSUVZUTVDNDJMWTVBRElYM01YNUJJWjZaMjNQS1lUSDNQUkRPWUZPNzZMWkgyWFJQS0ZRR1VHWkZIVFZORzY3NENOSjZSTFNKSzNWUFo1QjNaUUVGQTJRR08yR0wzS1lZTk5QNDZGVURFQjZBNVFKRjRDVUk1Q1I0UTNCVUZCSTZGVUNTWkw3VTNMUkM1UEdTRUM1MktCV1oyMlNDWlhSWUlSTFlPNlRBNERKMkNGQ0pONjVDNDdUUEhGU0lJNUs2VkZTT09QU1pPVUZYVUlUQlNGUVFMTk43TkJDS1ZPSlpaUURDSDdJTEtVRE9IUE5DUTdWRTNOVlZNSldaMkJQMkM1VE1WVk9JSDNEVjVDSkYyQUpGUjVTNjRKQVRFRUYzNkNHU0dYMkM0TkdENU1RVk00NEY1RlpRWlpPTDZORUgySFRZNDY1VDNMS0xJQVgzVENXUkJIVDZGNTZCWFNVWVVKS0tKUDNCTUZNUldCQ1FMNVkyVFhLTDdKNUpWUUpPQUc1SkRMR1hCR0M1S0g3R0tUNU5ZRlRVWEJLUFVWNk5MNVlHSjRHRlEzRVg1RllHVUVSU0VYNUpNQ0lLTkRVNURYWUFLS0xBNjVPTks2R1I0WFY0WlhPV1VTUVJVU0xUWENPUzdGQkkyM01WM0Q1NlFFRjVXREZSTzdQWldYU05YWFY1QURPUFBLWEJaTElUNjY0RFQ2RjJHWVRKV1lJRUFFSFo3WTdFVzJQMkRVT0FONlZCNFZSTjMyMkpPRERYT0ZHTEJNSDIzTTdLVUEzNU1NN05RNE1OQjNTN01XUFpZSFlQV05YWUU2REFYUllJVDZaUEpXNzVMM1lGUUJRV0VMSkhXT1NCNzZMWVI2R1pYQ0NVUFZCTVBHTVNCRlhLUEtaSEZEWEJNVEVPUjMyTEFDVUxRVEpBNzJOREhGR1dQRExDN1BNM1BWWUkyRzZIM0cyNk1KS1RNNlhaNE03U0YyUkdBWk5RMlpWQzIzRjZCRkpLTkJSV1pWRkVNSzdaVkoySTNBRkxTUEVGSTY0SFQzNkJKV0pEQzZMMzJHQUtDTDRQWEUyR01UT1ZQQ1kyWldGQUdTSFNLNERRV0xVNk00WklPVUhNUTdaVktTSlNQMlpUS1FHWFVDR0tNRzY0RU9HSkpCNDRUTzVFWkpEU0QzT09LUjZKRkZRVEVWRlpMVTQ1M1FUSkVQS083VE5ZMlMzNlM2Tkk0MzdBMzJEV1ZCWUg0VFpKTk9FT1NESDJVMkhBNk1MNjRPVDNSTlFBUENZMk9LM1o2S0ZIREZHQ0pCVDZPNlNUVk0zWllNTldVU1BIM05TRzRSRUlHSDNCNEFTTkE2WERCU0xHRk1XUTRSNk5JSEZMTTRPVlRXWTNWRFE2SENYVUFaM1BZNVlTVEgyV0VQTlFNVVlHRTU1UkNQRTdSNlhGVU1CUUZJSzdSMzNFS1lXRTIzUlMzVkZBNkxVRkRRVlQzVzNKRTVJNVQzRlI0WUYzUVo3SDdGUlVDNlFBV0pNNEY0T1RVUFdNTjYyQzJBQ1JFN0tNMkhMWDVTNDJKTDdCVEFCSkRUUlpOMkJOTDZYWVhVS0MzUUhMQTJISFRaNUdXRlJXSk1QNklZS0w3U05HUlVGRzIySjZSRkxCVFRIM1NZWllINjJNNks3SEFaNEdUN0VDU1hRSFFSRkxLUzRLT0ZNSEVCWEhaN1RHWDUzRUkyM0M1UTc2QTJIRkJURDZDUzVUNkJTSFM2QldYR0hGRkhYNkdGNVNPVE01U1hWVEZFRlRMWEtXTjZQVTNNU0lIVUIzM05WVDc1QVJESVE3QldIM0U3VkdJRkJJVVAyRzJZVjNIWFRTR1VIRklUVVE0STNWR1ZMSkJEMlJGUEJTNk5PTlQ1Q1RaRDJSSTM3Wk5GQlFXSTZISjVBMzZGUkhBRVhSN0NCUE9QS0NNT1dESlNNN09HS1RFT081M01NRko3SVNDVkhKWEVVM1pQTVJINVZBRjJTT0NFM0NRV1RBRlRYUlJHTTRMVEYzVUhEQVVURERYRUNPTk9XVUxUSDc3NkJMS0lETkhJWFZBS1Y2TU0zTzZJQUg2VkQ0VUNSSzRCRFRDT0tOVDNXR0RNVFVGUlNHQVA1MjQ2VkVMVDJIMkdZRktQMkJHNURMRzVHUTJBT1gzWldYMkxNWDNIUk5ISVlKVEtERVBUTjU2NlhJVE1WRDQ3S1RYUFdXTjVZM1o2S1dRM1pWRkpQQVFLSE0zTEdaWDdaSURQQTJXUTNKV1A1VVNNTFBDRkU1VlhNTlFVSzVUUktLRVpOT1pDQlRURUJZWUVBTDc1VjRVSU9DNUE3WVNaRUtYRUc1SzJQTDVVT1FPSEhRWVpCWFFUSTNLTEZYVDY1QTM0RDY1TENJV0dVM0lZUFdaSkRERFdJSVo2SjdSNkkzWkNVWkdCVTdXN1JPVDNKTEdLUFhaNUZLTkpFU1ZEVkRDUEtCMjJDR0JVNEpVVFM0T0Y2TTVPWkZKVjZKRkNLUDY1V1FaVFdEVVBGWE9TQ1oyNTZMVU5ERUIzMk1CR1FMQUpEVU5XS0xNWUxPWDVGU1E2SlBSMjNQRllOWVBENUk0NE1VQ1g0TUNFMlZQSU9QS1Y3RlcyNFJXVExTTFpKWjJNT1BOR0NPSzNWTVY2REQyTTVNU0o2UkxZVVFUTk5BR1kyUEU2VjZLT0VKRUFMM1dKRjJQRDRCNzdTNzRKTk9SVlU3STJHNTdUU0dOUVBaSFpYNkdaWkVLQTRNS0xSUVRGT1BLSlA2REQ1N0hTUUQzU0VWV0FZVFRFRVZYTUtGU05MQjJBTVZTSzROTjdCNVZHQ0NDWTJBT1o2SFY1UE5DUzZRTk9SQzRYMlhDSEpPNE81N1NKRFkzNUJPRkU3VEszTUFWTjZIWlhTRVZJVTY1MjQzNENIQU5HRFdNNlNHRFhUWEtVUzRYU0RRRFpPTzRTVUZRWTVMWFZIT0xMUEpNM080RFpUWlRXUlVFR0Q2VkNTUEo0TERJMkdXNERZQlZXVE81VktOVFNHNko2NU5LSEhIVUVPV1NJSUZZNlU0TktHTzVWRExXTUpZWExBQzZSUUpMUVVXTDVOVFpJMlNZU1BXU0hTSFdYSVFZV0czVE9CU0FNMkcyNVkyRFpRQkpTTEVUUkhUUDNHNkUyNExQU1RNNUxRU1VFRDIzUkFONUVVSkhKVjJER1VBS0JLN05UWEM2V1dTRklJWUlUUFRNV1NMWk9CRjY3QUdPNUNQSklPM0pRRkpYS1pOQjI1SU9YVFU2SUtXSElBWTRZUzJQN0JVSEJTUE1MV1pVU0FQSjMzRUpOMjQ1SjZXNlczT0I2RzRISEFNSTRIV0xRWktRRTNOTE5ETFlOTFpKSEdMNExYV0g3WUZNU0pHSTVZVEsyWElQMzdJWUJST0dCV1QzRkpCSU1LQjJHQ01QVTI0Mk9ZTENJUlVSTVZNTjNIV1NLR0RBTjZBMlpZSlRVNzM3SkZISkxOTUZCR09ZWEhCUVRVTDNOSEhSQ1RTSVFMU0RBS1M3Qks3TURGTFhPWldETUVLVlUzUVlMT1BCSE9WVTNKRFJYMlBUU1k1REhWM0lZSUdYTUZZRlRISjdZSURRMjdETFNPVFhDSkNGNkVSVURBUzZaU0hNN0dWN0tVMkVOQkdaVlNPTE5QTlVOTEZRUDY3S0tZUEZXUlZHS0wzMlNUTFhMVUNJU1hSQkI2NEtPWjc2WVpETERTUVZZWUhYR0Q1N09EMkhQRjc0U1NBSk8yQk9OWkRTRllHWFdZN0xDSVg1R043REdIUUJYTDU3WDdOQ1JYU05TVVJHNEc1TjUyQ1FXTVg0RDRLMkhFWlhaVVJPRTNQMkJINVpNU1lYNVdKRlBOUEZWTkJPWEU3QlFISkNQWUJPWUUyQkNEWTdWWUhFQ0JIQ01QR1dVUTdKSUIzN1lVMk9ZTEpSNFRHNzNSTTM0R05TWEs3Mk9OS1dNU1ZXMkVINU9XREVTVDU3WEJDS1BFSzVMVVdQTFRMVk9GUVIzR0M3TlJJUlJMSldYM1paV05USUlCTEQ3TE5IRE5NN1BYQ0daSFBUM1NQSzVaQjJDWUpXS0hWTU5UQkxOMlI0QVJYVUpSUldYS0k2VEpPNFpMT0lBTjdVRDM3N0lOUkpMUUpBTkZHVUVNNlBUTVpQNVMyTU9KU0hBUElYUzJVQkJQUEFPUlkzWTRRTUwySEdUVjQ1VVFHV1pBTjU3MlBXVTZPSjVWUU9FNVFJTjZTSE5PT1RPU1JQRkNHNTNLVkVBWFQzMkhDWjRZVDUzTzJNQURYVElGV0dNU1dQRTVVUExNUjVKQllJVkVKR0NQNDVVS04zREk3NVBUV01aMkNDMjc3Tko0NENBUE9DVlMzV01YNFNCRk81UzdURldGSEpPNklUVlpRSzJWS1RBWUhDWTRPQkpFVkNYU1BFMkYyNUVRUDRSRFFPQUFWVE9TQ0FDRUYyNjNZNjJWTEpTTkQ0WFA2TURGTDZOSllFN1A0WVBERVBaTzdUSURCSUVQUEJVVkVIWUlMVU9ZTTdQU1NGREVRNUVIVkpWNzNJRU5JWDdBR1RDRjZDSU9NQTVYQ1lVWEtERTRBQ0dVU0daNFdJNDNYVFJITE9LTEpVTkVWNU5ZM01LQ0lNWktGQUpMRkRINkRPSVJHUEdCSDdEVTNBWTZOV05YRkdOUjdGUUtaNlBJUk5YMlQzQVhOSDJQTlhQWTJPS1FGREtJN0tJTzNRT1ZPUFkyR0E0UjVISUNNVk9ERUNPWVFOVE5aQ1g3WUxMQUpPVFdLVFVLR1RST0ZBR0xYR1FPNFdTSlpZRTVTTFBVSkNRRlpPWEpZS0hIN1dMNDI3RlJJN0ZCR1dLREZEWDVKSElUUVRCWFVaTTVHRzZUSkpaRFBHSDNKSzNFSk1GWlJMREdKVDRVV1lPNlVYM0xKTTc1UVdYUVhFRFZRMk9OMko2VUdQTVVWUFBaUVhYUkxBUUpaMjdEWU9LSVBQWUY2UlJVNzZGVUpaWFhCT1dMTVRESjdDTk9MNFpEVlFQM1NVQ01aSk5FNENPUFVPNTUyRzVMM01IUEdVRzJKQ0JMNlFPV0dRNEJGSkRZTDM2T1dUQUg3T1lWWklWVFhXSVNHVkRMQkpQVURKSzVRTENSSEoyVVlGNzVRTzJZRVdPQ0VON05MTVpFRkM1RUs1Qk9SMkw1N05ZQUpIVzNUSkxMVVRBSVZZTFdJSkRDVlRJTlYzWDNMNVg0Qlo3TFBXVklYTVFZQ0lENEdYS0tYNkRCRk00T1pTNEtUUFdFUzQzVFBJWlBJUVQ1QUk0UFRLWkdSTVA0VUc0MkNSS1RNQjVKTE1NSVNNMlJMWEJURU9TRTZHMlZPQUNTWldST0E0Q1NBVDUzNjZCRjVFWEhSNEpWR0tUTVBWVEhJUTY2R0tMV0paR01FVzZDVjJRWVFUMjJVWVRINDJQSE9HMzVFRDJGVjZSWUE3Vlc2U0ZHRkRKUzRMVVA2QVZXUVpBVUhXRlRNN0xMMjVRS1dLQ0ozRzdJWUVGSERRSkFZRzdVSFQyUzNXVlhUNU1XVEtYRDVNM0VWVkdDTENWMkFNVlRCU01QTk1STTM1QVdCQkVENDdDSVNNNVg0NzZQQTNXS0haVDJHQzNNWU9RRUhVNEkyWE41MlFOVkpGWEhBVlZKV1MzNFdCMjJaRjJTQUE1M1JYQTRIQ1k0SEVCSk9IU1hCNzQ3QTdHRTM0MldXSTVKNkxIQUg2UjdJRFhaTlpRTUlMRVZXRjNUUTdaVVpaWFRDQUg2VVdHR1ZMQ1gyVUo0SkFWNFFKRlNJWlc3NFRHWE5YWVlES1I1TjNJRFgzM1VFNEtZWlhQTUNMTFMyM0dOUlFBVVdKWlA2UU5WR0tWUFNCQ0ZHVDVTR0JRM0VaR1E2N0FaWUEyMkNKMllaU0pETVJJTks2V1hMNldBNEQ1UlBITlJRTFlPU09INUNTQk42N0tCV0xVSVVLMjJaUlpQNkZUTUlWUFk1TkxDUzM0NzdZS0JQQ1FIRFBIU0U3RUxWNUc3T1dFUFRGWk0yQVI1SUxNUjNVS0dWNTVCMzMzVTdYV0hQRko2U0lYREZUUVdJMlQ0NEhHNzNZWDRYWFFUV01QTFJGUlJPWFpaTzJYVElQTkRHWjU0M1FIUUVaN1IzREJWNkxEU042SENCV040N0ZDNFlUSkpXTlo0MklITzJaWDdDS0dEMkxITklINk1WWDJDR1VIVDJaSU4yN1NPRTJCRTVGQTM1RERNNkNMSFpaQzZEN1dWRkxBV0ZITk03T0hIR0RHU0dNU1FaRzVaVFFLSEYyWkxLU0dQMlpGU1FMN1JaSjNMVUVLTjVDTUxSUERJTkNLNllHMlhGRFBCUEtGS1o1NkczTFIzWUhWQUVMR1NLV1IzVENQNEFBSDc2NEpCRlYyTlRVREJWVlVJWkVTR1JFNVhOQ0dNRkxQTUI1TlZKTDRQS1lWVFVQMjVHWU9PN0xKU0lXWktHVDc0M0JaSEQ0RzMzNEJMSzJMUFg2N1hBVFJTR0JUQTJVQkdJNVdBSVREU1BJWDNHT1JZUUg0VTJJRFo3RVdaTkpIVlM1UUJJNzRPN0tQRjVBVEpEQUpTN0szRTJITkdCMlRENjdQTlNHVEo2WldTTFlEN0xZTFVIWFpOVEpKVVhaSkRGVUhMRkRKTUNNQ1VGV1pDSTc1UzJORklDQk1WVDZOUENFTVZFNDVMWEJRWlZJSkMzMkhVUUpYRFlXTkhDQVJYV0VPUVEyWklBQVdTNVdQSTJQM0c1Sk5WS1U2NkZDNkRTS1QzNEhKU0RZSUVKVEU1R1FNRUxTUUFYQzJJWUJNNTI0SVhIRk9VTFZLQ0JDVk5PQU0yN1ZOWVo3NDREUVZLT0xNQlFXSlM3Q0VFU1hDVEhZRVRCVkFTNVpUTlU2S0dGR1JGQUJFVk1ENEdCTVJKNDdKRkFGQlNTRUtNTjRTSDNQUEFFTzdNTFNNR0kzNTNDSEY0Q1pQVEI3R1RaQ0tRTUtBTkVVWkVXNkZNUUxEUDRGMkhYTFVIR0tDRjJCSEdYS0JYVUtGV0xJVzJHVk9CNktCR0pOSVlXQVo1UU9PSTYzTUpSWkg0M1NKUUlJSlozT09NVDJVQTRLREdST0dXU0FXN1ZWUU9RS0ZPQlROVU1DWTZXT1I2R0ZKNU5HVUg3TkpHWE5GQVFQTUZSUFVRS0pOMlpENkhZR0JDRFFOWlZSNDZLQ0c2MjNURDZWVlIzWERQQzJFVlFKVllHUFQ2NVVaVk9HUEIyUlNFQVlTNVE3WFZFREJWRVZUQVBOWkJEQ01OSzQ2UjRIM09XWVpDUk03MlJFSFhKM0tRSjJOT05SN1NYQkY2UUVKUFhSSVVRN1I0NEROMk9QRDJKVFZVSEVJM1NMSFVBNElTQ0s1Q1JCT0pSNFQ0SFU2SlJQUlJVWEhRVU9BU0pONloyMk5KVVhQSURQTU1aMkhNRlBVWlFTSEhYVVFMTkVWRElXWFBWQldQM1I2SUxEQk9QNFNDT0dPTE9aU0ZNNERDRldXMktIS1dQSFNQQ1pVNko3SVFRUEI2V0lFRk5PQlpLTEhMNDZEUkpHWEpBTkVDQU5XN0NVRjdVQVgyT0RWM1VYU1hSRloyS09BSUNQU0VGRDJaVzZXT1lCNEVFM01TQ1lORDZOUlYzQUdON1dHNUo2U1FIWVpQM1c0QjZWVEhBNkIzV0VQSjdYUEI1RzJDN1ZCVFVaVzVVU0hOUFNCSjdONDZJSVVZVFZGN0M2S1pUNEJLREpMSkRSR1ZVNUlOWUdNVEJJVVZYN0wyWTdBNkkyRlhGNUhSRzNHNFY0TUdXVktZWEFURDdMVlpKS01VTlFZQldDNlBSNVBOQ1dONkdLWFVMTVNQUk82VVhKS1dKSVBWRVBWUFVTUVpONUVSSEJJSEc1QzZGUDMySk1WQUtFQ0NJNVM2TlNCQlBJTllVQVBKQ1JUNkxXQVZUVTdDS0ZZVkFPWFhVQVlZMk1KVUo3QVRUUjJFQU9RU1NSVVpDM1hCSUlBTU1TR0VVWTJFWEJRVkJGUU1VNFBIRVNRQUVXVlFSSVNRRERFSVJKVFRNVzNYT0lLVVBEQklEQkZZUFVENjdYMzc3TzNYNzU3SFoyUDdNUDZKSUxZR1M3Nlo0TEo3NUtUNUhSNlY2VVAzNTdTSUgyUFJKTUcyMzdPUFAzN1o2SzROWDVDTkxKTjdMNzVKNTczNllUSVA0N1pISkg3NjMzUzdQNzY3N1E3UFQ1N1o1NjNONzJSNzNaVjdDM1AySjY1Rjc3NlI3NzdYNlA3NktINzZESjI2TlVBVT09PSIpKSkp'))
