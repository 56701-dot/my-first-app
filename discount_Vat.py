import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7% และส่วนลด")
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
discountpercent = st.number_input("กรอกเปอร์เซนต์ส่วนลด :")
discountprice = price * (discountpercent//100)
vat = discountprice * 0.07
net_price = (price-discountprice)+vat
st.header(f"• ราคาสินค้า: {price:.2f} บาท")
st.header(f"• เปอร์เซนส่วนลด: {discountpercent:.2f} %")
st.header(f"• ส่วนลด: {discountprice:.2f} บาท")
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นายธีรภัทร ทิพย์พรหม เลขที่ 37  ม.4/5")
