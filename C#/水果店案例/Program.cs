using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ExampleFruit
{
    // 要求：
    //1.程序应该提示用户当前的余额为0，并允许会员输入充值金额，然后告诉用户当前余额为多少。
    //2.程序应该展示商店中的商品信息，内容为“菠萝：15元，草莓35元，香蕉10元”
    //3.程序应该使用枚举来表示商品类型。
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("当前会员卡余额为零，请输入想要充值的金额：");
            string money=Console.ReadLine();
            Console.WriteLine("已充值{0}元，当前余额为：{1}",money,money);
            Console.WriteLine("当前做活动的水果有：");
            Console.WriteLine(FRUIT.PINEAPPLE + "：15元");
            Console.WriteLine(FRUIT.STRAWBERRY + "：30元");
            Console.WriteLine(FRUIT.BANANA + "：10元");
            Console.ReadKey();
        }
    }
    /// <summary>
    /// 水果类型
    /// </summary>
    public enum FRUIT
    {
        PINEAPPLE,
        STRAWBERRY,
        BANANA
    }
}
