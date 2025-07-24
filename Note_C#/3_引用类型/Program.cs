using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3_引用类型
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //introduceObject();
            introduceBox();
            Console.ReadKey();
        }
       public static void introduceObject()
        {
            object a = 10.8f;
            Console.WriteLine(a);

        }
        public static void introduceBox()
        {
            //装箱与拆箱
            //把一个变量转成 object 类型称为装箱，反之则为拆箱
            object obj;
            int ba = 8;
            obj = ba;
            Console.WriteLine(obj);
            //拆箱
            int x = (int)obj;
            Console.WriteLine(x);
            // other 如果可能转成布尔
            object y = 0;
            bool f=Convert.ToBoolean(y);
            Console.WriteLine(f);
        }

    }

}
