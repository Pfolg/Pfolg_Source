using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SecondCsharpEnter
{
    internal class Program
    {
        static void Main(string[] args)
        {
            introduceInt();
            introduceFloat();
            introduceBool();
            introduceChar();
            introduceEnum();
            introduceStruct();
            introduceInOut();

            Console.ReadKey();


        }

        public static void introduceInt()
        {
            Console.WriteLine("\nintroduceInt");
            Console.WriteLine("整数类型\nYou can find reference at https://learn.microsoft.com/zh-cn/dotnet/csharp/language-reference/builtin-types/integral-numeric-types");
            sbyte a = 5;//-128——127
            Console.WriteLine("a=" + a);

            byte b = 5;//0--255
            Console.WriteLine("b=" + b);

            short s = 10000;//-32,768 到 32,767
            Console.WriteLine("s=" + s);

            int i = 800000;//-2,147,483,648 到 2,147,483,647
            Console.WriteLine("i=" + i + "\n……\n");

            var decimalLiteral = 42;
            var hexLiteral = 0x2A;
            var binaryLiteral = 0b_0010_1010;
            //前面的示例还演示了如何将 _ 用作数字分隔符。 可以将数字分隔符用于所有类型的数字文本。

            //整数文本的类型由其后缀确定

            //如果文本的值不在目标类型的范围内，则发生编译器错误 CS0031
            //还可以使用强制转换将整数文本所表示的值转换为除确定的文本类型之外的类型
            var signedByte = (sbyte)42;
            var longVariable = (long)42;

            //若要在运行时获取本机大小的整数大小，可以使用 sizeof()
            //Console.WriteLine($"size of nint = {sizeof(nint)}");//“nint”没有预定义的大小，因此 sizeof 只能在不安全的上下文中使用
            //Console.WriteLine($"size of nuint = {sizeof(nuint)}");

            // output when run in a 64-bit process
            //size of nint = 8
            //size of nuint = 8

            // output when run in a 32-bit process
            //size of nint = 4
            //size of nuint = 4
            // 数值转换 https://learn.microsoft.com/zh-cn/dotnet/csharp/language-reference/builtin-types/numeric-conversions




        }
        public static void introduceFloat()
        {
            int a = 0;
            Console.WriteLine($"\nintroduceFloat{a}");
            Console.WriteLine("浮点类型\nhttps://learn.microsoft.com/zh-cn/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types");
            //不带后缀的文本或带有 d 或 D 后缀的文本的类型为 double
            //带有 f 或 F 后缀的文本的类型为 float
            //带有 m 或 M 后缀的文本的类型为 decimal
            double d = 3D;
            d = 4d;
            d = 3.934_001;

            float f = 3_000.5F;
            f = 5.4f;

            decimal myMoney = 3_000.5m;
            myMoney = 400.75M;
            Console.WriteLine((decimal)d + (decimal)f + myMoney);

            //科学计数法
            double d1 = 0.42e2;
            Console.WriteLine(d1);  // output 42

            float f1 = 134.45E-2f;
            Console.WriteLine(f1);  // output: 1.3445

            decimal m = 1.5E6m;
            Console.WriteLine(m);  // output: 1500000
        }
        public static void introduceBool()
        {
            Console.WriteLine("\nintroduceBool");
            //bool 类型关键字是 .NET System.Boolean 结构类型的别名，它表示一个布尔值，可为 true 或 false。
            //若要使用 bool 类型的值执行逻辑运算，请使用布尔逻辑运算符。 bool 类型是 比较和相等运算符的结果类型。
            //bool 表达式可以是 if、do、while 和 for 语句中以及条件运算符 ?: 中的控制条件表达式。
            //bool 类型的默认值为 false。
            bool check = true;
            Console.WriteLine(check ? "Checked" : "Not checked");  // output: Checked

            Console.WriteLine(false ? "Checked" : "Not checked");  // output: Not checked

            //do you want to know more？https://learn.microsoft.com/zh-cn/dotnet/csharp/language-reference/builtin-types/bool
        }
        public static void introduceChar()
        {
            Console.WriteLine("\nintroduceChar");
            //char 类型关键字是 .NET System.Char 结构类型的别名，它表示 Unicode UTF - 16 字符。
            var chars = new[]
                                {
                                    'j',
                                    '\u006A',
                                    '\x006A',
                                    (char)106,
                                };
            //对于 Unicode 转义序列，必须指定全部四位十六进制值。 也就是说，\u006A 是一个有效的转义序列，而 \u06A 和 \u6A 是无效的。

            //对于十六进制转义序列，可以省略前导零。 也就是说，\x006A、\x06A 和 \x6A 转义序列是有效的，并且对应于同一个字符。
            Console.WriteLine(string.Join(" ", chars));  // output: j j j j

            //do you want to know more？https://learn.microsoft.com/zh-cn/dotnet/csharp/language-reference/builtin-types/char
        }
        public static void introduceEnum()
        {   
            Console.WriteLine("\nintroduceEnum");
            DRINK drink1 = DRINK.WATER;
            Console.WriteLine(drink1);//输出 water
            Console.WriteLine((int)drink1);//转为 int

            DRINK drink2 = DRINK.MILK;
            Console.WriteLine(drink2);
            Console.WriteLine((int)drink2);
        }
        public static void introduceStruct()
        {
            //结构体介绍
            //https://learn.microsoft.com/zh-cn/dotnet/csharp/language-reference/builtin-types/struct
            //https://www.bilibili.com/video/BV1YmzQYgEHD?p=19 视频讲解
            Console.WriteLine("\nintroduceStruct");

            Vector3 playerPosition = new Vector3();
            playerPosition.x= 0;
            playerPosition.y= 0;
            playerPosition.z= 0;
            Vector3 enemyPosition = new Vector3();
            enemyPosition.x= 1;
            enemyPosition.y= 4;
            enemyPosition.z = 9;
            Console.WriteLine("当前玩家的坐标是({0},{1},{2})",playerPosition.x,playerPosition.y,playerPosition.z);
            Console.WriteLine("当前敌人的坐标是({0},{1},{2})",enemyPosition.x,enemyPosition.y,enemyPosition.z);


        }
        /// <summary>
        /// 饮料
        /// </summary>
        public enum DRINK
        {
            WATER,//水
            MILK=18,//牛奶
            COFFEE,//咖啡
        }
        public static void introduceInOut()
        {
            Console.Write("\nintroduceInOut\n请输入一个数字：");
            string balabala=Console.ReadLine();//这两行组合起来不就成 input（python） 了吗？哈哈哈哈哈哈哈哈哈！！！！！！！！！！！
            Console.WriteLine("您输入的数字是："+balabala);
            //输出 输入的内容
            //Console.WriteLine(Console.ReadLine());
        }

    }
    //https://www.bilibili.com/video/BV1YmzQYgEHD?p=18 枚举类型讲解
    enum Season
    {
        //https://learn.microsoft.com/zh-cn/dotnet/csharp/language-reference/builtin-types/enum

        //枚举类型 是由基础整型数值类型的一组命名常量定义的值类型。 若要定义枚举类型，请使用 enum 关键字并指定枚举成员 的名称：
        Spring,
        Summer,
        Autumn,
        Winter
    }

    //默认情况下，枚举成员的关联常数值为类型 int；它们从零开始，并按定义文本顺序递增 1。
    //可以显式指定任何其他整数数值类型作为枚举类型的基础类型。 还可以显式指定关联的常数值，如下面的示例所示：
    enum ErrorCode : ushort
    {
        None = 0,
        Unknown = 1,
        ConnectionLost = 100,
        OutlierReading = 200
    }

    struct Vector3
    {
        //三维坐标 结构体
        public float x; public float y; public float z;
    }

}
