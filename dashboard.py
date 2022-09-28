#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:56:37 2022

@author: lazyrook
"""

#######################################
#import the libraries
#######################################
import streamlit as st
import yfinance as yf
import pandas as pd
#######################################


st.title("Group 5's SENSEX Dashboard")

tickers = ("^BSESN","ASIANPAINT.BO","AXISBANK.BO","BAJAJ-AUTO.BO","BAJAJ FINSERV","BHARTI AIRTEL",
           "BHARTIARTL.BO","DRREDDY.BO","HCLTECH.BO","	HDFC.BO","HDFCBANK.BO",
           "HINDUNILVR.BO","ICICIBANK.BO","INDUSINDBK.BO","	INFY.BO","ITC.BO","KOTAKBANK.BO",
           "LT.BO","M&M.BO","MARUTI.BO","NESTLEIND.BO","NTPC.BO","ONGC.BO",
           "POWERGRID.BO","RELIANCE.BO","SBIN.BO","SUNPHARMA.BO","TCS.BO","TECHM.BO",
           "TITAN.BO","ULTRACEMCO.BO","","","","")

dropdown = st.multiselect("Pick your stock", tickers)

start = st.date_input("Start Date", value = pd.to_datetime('2022-01-01'))
end = st.date_input("End Date", value = pd.to_datetime('today'))



def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod()-1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    #df = yf.download(dropdown,start,end)['Adj Close']
   df = relativeret(yf.download(dropdown,start,end)['Adj Close'])
   st.header('Returns of {}'.format(dropdown))
   st.line_chart(df)