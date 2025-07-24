using System;
using System.Collections.Generic;
using System.Linq;
using System.Media;
using System.Text;
using System.Threading.Tasks;

namespace _8_匿名
{
    internal class Program
    {
        static void Main(string[] args)
        {
            #region 匿名类型
            var v = new { name = "Tom", age = 1 };
            Console.WriteLine(v.GetType());
            Console.WriteLine(v.name);
            var m = new { name = "Sam", age = 18 };
            var vm = new { v, m ,c=1.3f};

            Console.WriteLine(vm.m.age);

            Player player=new Player();
            var mPlayer = new { m, player };

            //数组 每个元素类型和名称要一致
            var array=new[] {
            new {n="1",m=2},
            new {n="3",m=4},
            new {n="4",m=5}};
            #endregion

            #region 匿名方法
            MyTestDelegate mtd = delegate (int n)
            {
                Console.WriteLine(n);
            };
            mtd(1);

            //way2
            Func<int, string> func = delegate (int x)
            {
                //Console.WriteLine();
                return x.ToString()+"h";
            };
            Console.WriteLine(func(10));
            //way3
            Action act = delegate { Console.WriteLine("w"); };
            act();//out w
            Func<int, string, float> func1 = delegate { return 1.2f; };
            float a = func1(1, "h");
            Console.WriteLine(a);
            #endregion

            #region lambda表达式
            Func<int,int>square=x=> x*x;
            int r = square(5);
            Console.WriteLine(r);

            Func<int, int, string> add = (x, y) => (x + y).ToString();//左边参数，右边方法体
            Console.WriteLine(add(1,2));
            #endregion

            Console.ReadKey();
        }
        public class Player { }

        #region 匿名方法
        //定义委托
        delegate void MyTestDelegate(int n);
        #endregion
    }
}
