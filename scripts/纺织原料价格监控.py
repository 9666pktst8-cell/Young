#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
纺织原料价格监控脚本
用于自动跟踪主要纺织原料价格变化
"""

import json
import datetime
import os
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum

# 价格数据存储路径
PRICE_DATA_DIR = "/root/.openclaw/workspace/memory/price_data"
os.makedirs(PRICE_DATA_DIR, exist_ok=True)

class FiberType(Enum):
    """纤维类型枚举"""
    COTTON = "棉纱"
    POLYESTER = "涤纶"
    SPANDEX = "氨纶"
    NYLON = "锦纶"
    VISCOSE = "粘胶"
    WOOL = "羊毛"
    SILK = "蚕丝"

@dataclass
class PriceRecord:
    """价格记录"""
    date: str
    fiber_type: FiberType
    specification: str
    price: float  # 元/吨
    change: float  # 涨跌幅度
    source: str
    remarks: str = ""

class TextilePriceMonitor:
    """纺织原料价格监控器"""
    
    def __init__(self):
        self.price_data: Dict[str, List[PriceRecord]] = {}
        self.load_price_data()
    
    def load_price_data(self):
        """加载历史价格数据"""
        data_file = os.path.join(PRICE_DATA_DIR, "price_history.json")
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # 转换数据格式
                for fiber_type_str, records in data.items():
                    fiber_type = FiberType(fiber_type_str)
                    self.price_data[fiber_type] = [
                        PriceRecord(**record) for record in records
                    ]
    
    def save_price_data(self):
        """保存价格数据"""
        data_file = os.path.join(PRICE_DATA_DIR, "price_history.json")
        data = {}
        for fiber_type, records in self.price_data.items():
            data[fiber_type.value] = [
                {
                    'date': r.date,
                    'fiber_type': r.fiber_type.value,
                    'specification': r.specification,
                    'price': r.price,
                    'change': r.change,
                    'source': r.source,
                    'remarks': r.remarks
                }
                for r in records
            ]
        
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def add_price_record(self, record: PriceRecord):
        """添加价格记录"""
        if record.fiber_type not in self.price_data:
            self.price_data[record.fiber_type] = []
        
        self.price_data[record.fiber_type].append(record)
        # 按日期排序
        self.price_data[record.fiber_type].sort(key=lambda x: x.date)
        self.save_price_data()
    
    def get_latest_price(self, fiber_type: FiberType, specification: str = None) -> Optional[PriceRecord]:
        """获取最新价格"""
        if fiber_type not in self.price_data:
            return None
        
        records = self.price_data[fiber_type]
        if not records:
            return None
        
        if specification:
            # 按规格筛选
            spec_records = [r for r in records if r.specification == specification]
            if spec_records:
                return spec_records[-1]
            return None
        
        return records[-1]
    
    def get_price_trend(self, fiber_type: FiberType, days: int = 30) -> List[PriceRecord]:
        """获取价格趋势"""
        if fiber_type not in self.price_data:
            return []
        
        end_date = datetime.datetime.now().strftime("%Y-%m-%d")
        start_date = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
        
        records = [
            r for r in self.price_data[fiber_type]
            if start_date <= r.date <= end_date
        ]
        
        return records
    
    def calculate_price_change(self, fiber_type: FiberType, days: int = 7) -> float:
        """计算价格变化百分比"""
        records = self.get_price_trend(fiber_type, days)
        if len(records) < 2:
            return 0.0
        
        latest_price = records[-1].price
        oldest_price = records[0].price
        
        if oldest_price == 0:
            return 0.0
        
        return (latest_price - oldest_price) / oldest_price * 100
    
    def generate_price_report(self) -> str:
        """生成价格报告"""
        report_lines = []
        report_lines.append("=" * 60)
        report_lines.append("纺织原料价格日报")
        report_lines.append(f"日期: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 60)
        
        for fiber_type in FiberType:
            latest_record = self.get_latest_price(fiber_type)
            if latest_record:
                change_7d = self.calculate_price_change(fiber_type, 7)
                change_30d = self.calculate_price_change(fiber_type, 30)
                
                report_lines.append(f"\n{fiber_type.value}:")
                report_lines.append(f"  最新价格: ¥{latest_record.price:,.0f}/吨")
                report_lines.append(f"  规格: {latest_record.specification}")
                report_lines.append(f"  数据来源: {latest_record.source}")
                report_lines.append(f"  7日涨跌: {change_7d:+.2f}%")
                report_lines.append(f"  30日涨跌: {change_30d:+.2f}%")
                if latest_record.remarks:
                    report_lines.append(f"  备注: {latest_record.remarks}")
        
        report_lines.append("\n" + "=" * 60)
        report_lines.append("价格预警:")
        
        # 检查大幅波动
        warnings = []
        for fiber_type in FiberType:
            change_1d = self.calculate_price_change(fiber_type, 1)
            if abs(change_1d) > 3:
                warnings.append(f"{fiber_type.value}单日涨跌超过3%: {change_1d:+.2f}%")
        
        if warnings:
            for warning in warnings:
                report_lines.append(f"  ⚠️ {warning}")
        else:
            report_lines.append("  暂无价格预警")
        
        report_lines.append("=" * 60)
        return "\n".join(report_lines)

# 标准价格数据（示例）
STANDARD_PRICES = {
    FiberType.COTTON: [
        ("32s精梳紧密纺", 29500, "盛泽市场"),
        ("40s精梳紧密纺", 31000, "盛泽市场"),
        ("32s普梳", 27000, "盛泽市场"),
        ("40s普梳", 28500, "盛泽市场"),
    ],
    FiberType.POLYESTER: [
        ("POY 150D/48F", 8000, "化纤信息网"),
        ("FDY 150D/96F", 8500, "化纤信息网"),
        ("DTY 150D/48F", 9200, "化纤信息网"),
        ("涤纶短纤1.4D", 7800, "化纤信息网"),
    ],
    FiberType.SPANDEX: [
        ("20D", 46000, "行业报价"),
        ("30D", 43000, "行业报价"),
        ("40D", 41000, "行业报价"),
        ("70D", 39000, "行业报价"),
    ],
    FiberType.NYLON: [
        ("FDY 70D/24F", 18500, "行业报价"),
        ("DTY 70D/24F", 19500, "行业报价"),
        ("锦纶6切片", 15000, "行业报价"),
    ],
    FiberType.VISCOSE: [
        ("粘胶短纤1.2D", 14000, "行业报价"),
        ("粘胶纱30s", 21000, "行业报价"),
        ("粘胶纱40s", 23000, "行业报价"),
    ]
}

def initialize_sample_data():
    """初始化示例数据"""
    monitor = TextilePriceMonitor()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 添加示例数据（过去30天）
    for i in range(30):
        date = (datetime.datetime.now() - datetime.timedelta(days=30-i)).strftime("%Y-%m-%d")
        
        for fiber_type, specs in STANDARD_PRICES.items():
            for spec, base_price, source in specs:
                # 模拟价格波动
                import random
                price_variation = random.uniform(-0.05, 0.05)  # ±5%波动
                current_price = base_price * (1 + price_variation)
                change = random.uniform(-2, 2)  # 模拟涨跌
                
                record = PriceRecord(
                    date=date,
                    fiber_type=fiber_type,
                    specification=spec,
                    price=round(current_price),
                    change=change,
                    source=source,
                    remarks="示例数据" if i < 29 else "今日数据"
                )
                monitor.add_price_record(record)
    
    print("示例数据初始化完成")

def main():
    """主函数"""
    print("纺织原料价格监控系统")
    print("-" * 40)
    
    monitor = TextilePriceMonitor()
    
    # 检查是否有数据，如果没有则初始化示例数据
    if not monitor.price_data:
        print("未找到价格数据，正在初始化示例数据...")
        initialize_sample_data()
        monitor = TextilePriceMonitor()  # 重新加载
    
    while True:
        print("\n请选择操作:")
        print("1. 查看最新价格")
        print("2. 生成价格日报")
        print("3. 添加价格记录")
        print("4. 查看价格趋势")
        print("5. 退出")
        
        choice = input("请输入选项 (1-5): ").strip()
        
        if choice == "1":
            print("\n选择纤维类型:")
            for i, fiber_type in enumerate(FiberType, 1):
                print(f"{i}. {fiber_type.value}")
            
            try:
                fiber_idx = int(input("请输入纤维类型编号: ")) - 1
                if 0 <= fiber_idx < len(FiberType):
                    fiber_type = list(FiberType)[fiber_idx]
                    latest = monitor.get_latest_price(fiber_type)
                    if latest:
                        print(f"\n{fiber_type.value}最新价格:")
                        print(f"  日期: {latest.date}")
                        print(f"  规格: {latest.specification}")
                        print(f"  价格: ¥{latest.price:,.0f}/吨")
                        print(f"  涨跌: {latest.change:+.2f}%")
                        print(f"  来源: {latest.source}")
                        if latest.remarks:
                            print(f"  备注: {latest.remarks}")
                    else:
                        print(f"未找到{fiber_type.value}的价格数据")
                else:
                    print("编号无效")
            except ValueError:
                print("请输入有效的数字")
        
        elif choice == "2":
            report = monitor.generate_price_report()
            print("\n" + report)
            
            # 保存报告到文件
            report_file = os.path.join(PRICE_DATA_DIR, f"price_report_{datetime.datetime.now().strftime('%Y%m%d')}.txt")
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\n报告已保存到: {report_file}")
        
        elif choice == "3":
            print("\n添加价格记录")
            date = input("日期 (YYYY-MM-DD，留空使用今天): ").strip()
            if not date:
                date = datetime.datetime.now().strftime("%Y-%m-%d")
            
            print("选择纤维类型:")
            for i, fiber_type in enumerate(FiberType, 1):
                print(f"{i}. {fiber_type.value}")
            
            try:
                fiber_idx = int(input("纤维类型编号: ")) - 1
                if 0 <= fiber_idx < len(FiberType):
                    fiber_type = list(FiberType)[fiber_idx]
                    specification = input("规格描述: ").strip()
                    price = float(input("价格(元/吨): ").strip())
                    change = float(input("涨跌幅度(%): ").strip())
                    source = input("数据来源: ").strip()
                    remarks = input("备注(可选): ").strip()
                    
                    record = PriceRecord(
                        date=date,
                        fiber_type=fiber_type,
                        specification=specification,
                        price=price,
                        change=change,
                        source=source,
                        remarks=remarks
                    )
                    monitor.add_price_record(record)
                    print("价格记录添加成功!")
                else:
                    print("编号无效")
            except ValueError:
                print("请输入有效的数字")
        
        elif choice == "4":
            print("\n查看价格趋势")
            print("选择纤维类型:")
            for i, fiber_type in enumerate(FiberType, 1):
                print(f"{i}. {fiber_type.value}")
            
            try:
                fiber_idx = int(input("纤维类型编号: ")) - 1
                if 0 <= fiber_idx < len(FiberType):
                    fiber_type = list(FiberType)[fiber_idx]
                    days = int(input("查看最近多少天的趋势 (默认30): ") or "30")
                    
                    trend = monitor.get_price_trend(fiber_type, days)
                    if trend:
                        print(f"\n{fiber_type.value}最近{days}天价格趋势:")
                        print("-" * 60)
                        print("日期        规格                 价格        涨跌    来源")
                        print("-" * 60)
                        for record in trend[-10:]:  # 显示最近10条
                            print(f"{record.date}  {record.specification:20}  ¥{record.price:8,.0f}  {record.change:6.2f}%  {record.source}")
                        
                        if len(trend) > 10:
                            print(f"... (共{len(trend)}条记录)")
                        
                        # 计算统计信息
                        prices = [r.price for r in trend]
                        if prices:
                            avg_price = sum(prices) / len(prices)
                            max_price = max(prices)
                            min_price = min(prices)
                            price_change = ((prices[-1] - prices[0]) / prices[0] * 100) if prices[0] != 0 else 0
                            
                            print(f"\n统计信息:")
                            print(f"  平均价格: ¥{avg_price:,.0f}/吨")
                            print(f"  最高价格: ¥{max_price:,.0f}/吨")
                            print(f"  最低价格: ¥{min_price:,.0f}/吨")
                            print(f"  期间涨跌: {price_change:+.2f}%")
                    else:
                        print(f"未找到{fiber_type.value}的价格趋势数据")
                else:
                    print("编号无效")
            except ValueError:
                print("请输入有效的数字")
        
        elif choice == "5":
            print("退出系统")
            break
        
        else:
            print("无效选项，请重新选择")

if __name__ == "__main__":
    main()