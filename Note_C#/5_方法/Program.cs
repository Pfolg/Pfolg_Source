using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace method


{
    internal class Program
    {
        static void Main(string[] args)
        {
            #region Test1();
            Console.WriteLine(MyTest(1,2));
            int a = 6;
            int b = 7;
            #endregion

            #region 如果函数有返回值，则不会修改a，b的值 条件是传递值类型
            Console.WriteLine(MyTest(a,b));
            Console.WriteLine(a);
            Console.WriteLine(b);
            #endregion

            # region 反之则会 条件是传递引用类型
            int[] c = { a,b};
            Test2(c);
            Console.WriteLine(c[0]);
            Console.WriteLine(c[1]);
            #endregion

            # region 按引用传递参数
            test3(ref a, ref b);
            Console.WriteLine(a);
            Console.WriteLine(b);
            #endregion

            # region 按输出传递参数
            float d = 0;
            Console.WriteLine(test4(out d, out b));            
            Console.WriteLine(d);
            Console.WriteLine(b);
            #endregion

            # region 参数数组与params关键字 参数不固定
            OutPutName("张三","李四");
            #endregion

            #region 可选参数
            showSomething(10);
            showSomething(100, 100);
            #endregion

            #region 递归
            Console.WriteLine(DiGui(5));
            #endregion

        }

        public static void Test1()
        {
            Console.WriteLine("你好，方法！");


        }

        #region 引用类型传参，无返回值
        public static void Test2(int[] a)
        {
            a[0] = 100;
            a[1] = 200;
            Console.WriteLine("已修改值");

        }
        #endregion

        #region 带参数和返回值的方法
        public static int MyTest(int a,int b)
        {
            int temp;
            temp = a;
            a = b;
            b=temp;
            Console.WriteLine("{0} + {1} = {2}",a,b,a+b);
            return a + b;
        }
        #endregion

        #region 按引用传递参数 https://www.bilibili.com/video/BV1YmzQYgEHD?p=61
        public static void test3(ref int a, ref int b)
        {
            int temp;
            temp=a;
            a = b;
            b=temp;
            Console.WriteLine("已交换值");
        }
        #endregion

        #region 按输出传递参数
        public static int test4(out float a, out int b)
        {
            a = 1.4f;
            b = 800;
            return (int) a+b;
        }
        #endregion

        #region 参数数组与params关键字 参数不固定
        public static void OutPutName(params string[] names)
        {
            foreach (string name in names)
            {
                Console.WriteLine(name);
            }
        }
        #endregion

        #region 如果参数给了默认值，那就是可选参数，放在后面
        public static void showSomething(int a,int b=10)
        {
            Console.WriteLine(a + b);
        }
        #endregion

        #region 递归
        public static int DiGui(int n)
        {
            if (n <= 1)
                return 1;
            else
            {
                return n*DiGui(n-1);
            }
        }
        #endregion
    }
}
