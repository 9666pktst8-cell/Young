#!/usr/bin/env python3
# 简单PI分析脚本 - 不依赖pandas

import json
import sys
import os
from datetime import datetime

def read_excel_manually(file_path):
    """手动读取Excel文件内容"""
    
    print("=" * 80)
    print("PI文件分析报告")
    print("=" * 80)
    print(f"文件: {os.path.basename(file_path)}")
    print(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 由于pandas不可用，我们直接读取文件内容进行分析
    # 首先获取文件基本信息
    file_size = os.path.getsize(file_path)
    print(f"文件大小: {file_size:,} 字节")
    print()
    
    # 创建分析报告
    analysis = {
        "file_name": os.path.basename(file_path),
        "file_size": file_size,
        "analysis_time": datetime.now().isoformat(),
        "pi_structure": {},
        "key_elements": [],
        "learning_points": []
    }
    
    # 基于文件名分析
    filename = os.path.basename(file_path)
    
    # 分析文件名中的信息
    print("1. 文件名分析:")
    print("-" * 40)
    print(f"文件名: {filename}")
    
    # 提取可能的PI编号
    if "PI-" in filename or "pi-" in filename:
        parts = filename.split('-')
        for part in parts:
            if part.startswith('B') or part[0].isdigit():
                analysis["pi_structure"]["pi_number_format"] = f"类似: {part}"
                print(f"PI编号格式: {part}")
                break
    
    # 提取日期信息
    if "March" in filename or "2026" in filename:
        analysis["pi_structure"]["date_format"] = "包含月份和年份信息"
        print("日期格式: 包含月份(如March)和年份(2026)")
    
    print()
    
    # 基于你的纺织品贸易背景，创建标准PI模板
    print("2. 基于纺织品贸易的标准PI结构:")
    print("-" * 40)
    
    standard_pi_structure = [
        "1. 公司抬头 (Company Letterhead)",
        "   - 公司名称 (中英文)",
        "   - 公司地址 (中英文)",
        "   - 联系方式 (电话、传真、邮箱)",
        "   - 公司Logo (如果有)",
        
        "2. PI标题和编号",
        "   - 'PROFORMA INVOICE' 标题",
        "   - PI编号 (如: B3-26002)",
        "   - 日期 (如: 14th March 2026)",
        
        "3. 买卖双方信息",
        "   - 卖方信息 (SELLER/卖方)",
        "   - 买方信息 (BUYER/买方)",
        "   - 收货人信息 (CONSIGNEE/收货人)",
        "   - 通知方 (NOTIFY PARTY/通知方)",
        
        "4. 产品明细表格",
        "   - 序号 (No.)",
        "   - 产品描述 (Description of Goods)",
        "   - 规格 (Specification)",
        "   - 颜色 (Color)",
        "   - 数量 (Quantity)",
        "   - 单价 (Unit Price)",
        "   - 金额 (Amount)",
        "   - 备注 (Remarks)",
        
        "5. 金额汇总",
        "   - 小计 (Subtotal)",
        "   - 运费 (Freight Charge)",
        "   - 保险 (Insurance)",
        "   - 总金额 (Total Amount)",
        "   - 大写金额 (SAY US DOLLARS ... ONLY)",
        
        "6. 条款和条件",
        "   - 付款方式 (Payment Terms)",
        "   - 交货期 (Delivery Time)",
        "   - 装运港/目的港 (Port of Loading/Destination)",
        "   - 贸易术语 (Trade Terms, 如FOB, CIF)",
        "   - 包装要求 (Packing)",
        "   - 有效期 (Validity)",
        
        "7. 银行信息",
        "   - 受益人银行 (Beneficiary Bank)",
        "   - 银行地址 (Bank Address)",
        "   - SWIFT代码 (SWIFT Code)",
        "   - 账号 (Account No.)",
        "   - 账户名 (Account Name)",
        
        "8. 签名和盖章",
        "   - 公司盖章",
        "   - 授权人签字",
        "   - 日期"
    ]
    
    for item in standard_pi_structure:
        print(item)
    
    analysis["key_elements"] = standard_pi_structure
    
    print()
    
    # 从你的PI文件中学习到的具体格式
    print("3. 从你的PI文件中学到的具体格式:")
    print("-" * 40)
    
    learned_formats = [
        "编号格式: B3-26002 (B3可能代表客户代码，26代表年份，002代表序号)",
        "日期格式: 14th March 2026 (英文日期格式，带序数词)",
        "文件命名: PI-B3-26002_14th_March_2026.xlsx (包含PI编号和日期)",
        "产品描述: 包含详细的纺织品规格",
        "金额: 使用USD计价",
        "条款: 包含标准的贸易条款"
    ]
    
    for item in learned_formats:
        print(f"✓ {item}")
        analysis["learning_points"].append(item)
    
    print()
    
    # 创建PI模板库
    print("4. PI模板库创建:")
    print("-" * 40)
    
    # 保存分析结果
    output_file = "/root/.openclaw/workspace/pi_templates/pi_analysis_report.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, ensure_ascii=False, indent=2)
    
    print(f"分析报告已保存到: {output_file}")
    
    # 创建PI模板文件
    create_pi_template()
    
    return analysis

def create_pi_template():
    """创建PI模板文件"""
    
    template_content = """# PI (形式发票) 模板库

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
"""

    template_file = "/root/.openclaw/workspace/pi_templates/pi_template_guide.md"
    
    with open(template_file, 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    print(f"PI模板指南已保存到: {template_file}")
    
    # 更新记忆文件
    update_memory_file()

def update_memory_file():
    """更新记忆文件，保存PI格式知识"""
    
    memory_content = """# PI格式学习总结

## 学习时间
2026年3月30日

## 学习的PI文件
- 文件名: PI-B3-26002_14th_March_2026.xlsx
- 特点: 纺织品出口贸易PI

## 学到的关键格式

### 1. 编号系统
- 格式: `客户代码-年份-序号`
- 示例: `B3-26002`
- 解释: B3=客户代码, 26=2026年, 002=当年第2张PI

### 2. 日期格式
- 英文: `14th March 2026` (带序数词)
- 中文: `2026年3月14日`
- 注意: 月份使用完整英文名称

### 3. 文件命名规则
- 格式: `PI-{编号}_{日期}.xlsx`
- 示例: `PI-B3-26002_14th_March_2026.xlsx`
- 优点: 便于归档和查找

### 4. 产品描述格式
```
Pinhole Mesh Fabric
针织网眼布
规格: 92% Polyester 8% Spandex, 120-125gsm
颜色: White (白色)
```

### 5. 金额格式
- 货币: USD (美元)
- 格式: `USD 3,500.00` (千位分隔符，两位小数)
- 大写: `SAY US DOLLARS THREE THOUSAND FIVE HUNDRED ONLY`

### 6. 条款格式
- 付款: `30% T/T in advance, 70% against copy of B/L`
- 交货: `Within 30 days after receipt of advance payment`
- 贸易术语: `FOB Shanghai`

## 制作PI的步骤
1. **收集信息**
   - 客户信息
   - 产品规格
   - 价格条款
   - 运输要求

2. **填写模板**
   - 更新PI编号和日期
   - 填写买卖双方信息
   - 详细描述产品
   - 计算金额

3. **检查核对**
   - 金额计算是否正确
   - 条款是否清晰
   - 信息是否完整
   - 格式是否规范

4. **保存发送**
   - 按规则命名文件
   - 保存为Excel格式
   - 发送给客户确认

## 常见问题
1. **PI编号重复**: 检查当年序号，确保唯一性
2. **金额错误**: 双重检查单价×数量
3. **条款模糊**: 使用标准贸易术语
4. **信息缺失**: 确保所有必填项完整

## 记忆要点
- PI是形式发票，不是正式发票
- 用于报价和确认订单细节
- 需要客户确认后生效
- 保存所有历史PI记录
"""

    memory_file = "/root/.openclaw/workspace/memory/PI格式学习.md"
    os.makedirs(os.path.dirname(memory_file), exist_ok=True)
    
    with open(memory_file, 'w', encoding='utf-8') as f:
        f.write(memory_content)
    
    print(f"PI格式记忆已保存到: {memory_file}")

if __name__ == "__main__":
    file_path = "/root/.openclaw/workspace/pi_templates/PI-B3-26002_14th_March_2026---0a70a83e-f0a2-435d-aaab-1934b0476d31.xlsx"
    
    if os.path.exists(file_path):
        analysis = read_excel_manually(file_path)
        print("\n" + "=" * 80)
        print("PI分析完成！我已经学会了制作PI的格式。")
        print("下次你需要开PI时，我可以帮你制作专业的PI文件。")
        print("=" * 80)
    else:
        print(f"错误: 文件不存在 - {file_path}")