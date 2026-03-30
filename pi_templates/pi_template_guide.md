# PI (形式发票) 模板库

## 基本信息
- **文件类型**: Excel格式形式发票
- **适用行业**: 纺织品出口贸易
- **语言**: 中英文对照

## PI编号规则
- 格式: `客户代码-年份-序号`
- 示例: `B3-26002`
  - `B3`: 客户代码
  - `26`: 2026年
  - `002`: 当年第2张PI

## 日期格式
- 英文格式: `14th March 2026`
- 中文格式: `2026年3月14日`
- 位置: PI标题下方

## PI结构模板

### 1. 公司抬头
```
[公司Logo]
LUSA TEXTILE (SUZHOU) CO., LTD
苏州鲁莎纺织有限公司
地址: Group 12, Hehua Village, Shengze Town, Wujiang District, Suzhou City
     江苏省苏州市吴江区盛泽镇荷花村12组
电话: 
传真: 
邮箱: yf63510038@163.com
```

### 2. PI标题
```
PROFORMA INVOICE
形式发票

PI NO.: B3-26002
DATE: 14th March 2026
```

### 3. 买卖双方信息
```
SELLER/卖方:
LUSA TEXTILE (SUZHOU) CO., LTD
[公司地址和联系方式]

BUYER/买方:
[客户公司名称]
[客户地址]
[联系人信息]
```

### 4. 产品明细表格
| No. | Description of Goods | Specification | Color | Quantity | Unit Price | Amount |
|-----|---------------------|---------------|-------|----------|------------|--------|
| 1   | Pinhole Mesh Fabric | 92% Polyester 8% Spandex | White | 1,000 kg | USD 3.50/kg | USD 3,500.00 |
|     | 针织网眼布          | 涤纶92% 氨纶8% | 白色  |          |            |        |

### 5. 金额汇总
```
SUB TOTAL: USD 3,500.00
FREIGHT CHARGE: USD 300.00
INSURANCE: USD 50.00
TOTAL AMOUNT: USD 3,850.00

SAY US DOLLARS THREE THOUSAND EIGHT HUNDRED AND FIFTY ONLY.
```

### 6. 条款和条件
```
PAYMENT: 30% T/T in advance, 70% against copy of B/L
付款: 30%预付款，70%见提单副本付款

DELIVERY: Within 30 days after receipt of advance payment
交货: 收到预付款后30天内

PORT: Shanghai, China to [目的港]
港口: 中国上海 至 [目的港]

TERMS: FOB Shanghai
条款: 上海离岸价

VALIDITY: 30 days from the date hereof
有效期: 自本发票签发之日起30天
```

### 7. 银行信息
```
BENEFICIARY BANK: JIANGSU SUZHOU RURAL COMMERCIAL BANK CO., LTD
SWIFT: WJRBCNBWXXX
ACCOUNT NO.: 0706678981420100397410
ACCOUNT NAME: LUSA TEXTILE (SUZHOU) CO., LTD
```

### 8. 签名盖章
```
For and on behalf of
LUSA TEXTILE (SUZHOU) CO., LTD

_________________________
Authorized Signature
公司盖章
日期: __________________
```

## 使用说明
1. 替换 `[]` 中的内容为客户具体信息
2. 根据实际产品更新产品明细
3. 调整金额和条款
4. 保存为Excel格式，使用相同的命名规则
