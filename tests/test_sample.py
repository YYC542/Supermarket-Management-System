"""
简单的测试示例 - 超市管理系统
这个文件包含基本的单元测试来验证系统核心功能
"""

def add(a, b):
    """加法函数"""
    return a + b

def multiply(a, b):
    """乘法函数"""
    return a * b

def calculate_total(price, quantity):
    """计算商品总价"""
    return price * quantity

def apply_discount(total, discount_percent):
    """应用折扣"""
    return total * (1 - discount_percent / 100)


# 测试函数
def test_add():
    """测试加法功能"""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    print("✓ 加法测试通过")

def test_multiply():
    """测试乘法功能"""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    print("✓ 乘法测试通过")

def test_calculate_total():
    """测试计算总价功能"""
    assert calculate_total(10, 5) == 50
    assert calculate_total(25.5, 2) == 51.0
    assert calculate_total(100, 0) == 0
    print("✓ 总价计算测试通过")

def test_apply_discount():
    """测试折扣功能"""
    assert apply_discount(100, 10) == 90  # 10% 折扣
    assert apply_discount(50, 20) == 40   # 20% 折扣
    assert apply_discount(200, 0) == 200  # 无折扣
    print("✓ 折扣计算测试通过")

def test_supermarket_scenario():
    """测试完整的超市购物场景"""
    # 商品单价
    item_price = 25.00
    # 购买数量
    quantity = 3
    # 计算小计
    subtotal = calculate_total(item_price, quantity)
    assert subtotal == 75.00
    
    # 应用15%的会员折扣
    final_total = apply_discount(subtotal, 15)
    assert final_total == 63.75
    
    print("✓ 超市购物场景测试通过")


# 如果直接运行这个文件
if __name__ == "__main__":
    test_add()
    test_multiply()
    test_calculate_total()
    test_apply_discount()
    test_supermarket_scenario()
    print("\n🎉 所有测试都通过了！")
