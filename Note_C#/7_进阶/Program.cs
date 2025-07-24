using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static _7_进阶.hhh;
//using mySpace.anothernamespace;
//using mySpace.anamespace;

namespace _7_进阶
{
    internal class Program
    {
        static void Main(string[] args)
        {

            mySpace.anamespace.aclass aclass = new mySpace.anamespace.aclass();
            aclass.func();

            mySpace.anothernamespace.aclass aclass1 = new mySpace.anothernamespace.aclass();
            aclass1.func();

            Console.WriteLine(hhh.h);

            PrintData<int> pd = new PrintData<int>();
            pd.SetNumber(10);
            Console.WriteLine(pd.GetNumber());

            PrintData<string> ps = new PrintData<string>();
            ps.SetNumber("hl");
            Console.WriteLine(ps.GetNumber());


            PrintNumber(256);

            A a = new A();
            a.Test<int, float, string>(1, 1.5f, "哈喽");


            #region 列表 自动扩容
            List<int> numberList = new List<int>();
            numberList.Add(1);
            numberList.Add(2);
            numberList.Add(3);
            numberList.Add(4);
            numberList.Add(5);
            for (int i = 0; i < numberList.Count; i++)
            {
                Console.WriteLine(numberList[i]);
            }
            Console.WriteLine("当前列表的长度：" + numberList.Count);
            Console.WriteLine("当前列表的容量：" + numberList.Capacity);
            Console.WriteLine("列表中的第零个元素是：" + numberList[0]);
            //numberList.Clear();//清空列表
            Console.WriteLine("当前列表内是否存在 1 ：" + numberList.Contains(1));
            numberList.Remove(1); //移除元素1
            numberList.RemoveAt(0);//移除索引为 1 的元素
            for (int i = 0; i < numberList.Count; i++)
            {
                Console.WriteLine(numberList[i]);
            }
            #endregion

            #region 字典
            List<Dog> dogList = new List<Dog>() { new Dog(), new Dog() };
            dogList[0].Eat();

            Dictionary<string, Player> playerdict = new Dictionary<string, Player>()
            {
                { "李华",new Player()},
                { "TOM",new Player()}
            };
            playerdict.Add("Pfolg", new Player());
            playerdict.Clear();
            playerdict.Remove("李华");
            if (playerdict.ContainsKey("TOM"))
            {
                Console.WriteLine("TOM在字典里");
            }
            Player p = new Player();
            if (playerdict.TryGetValue("TOM", out p))
            {
                p.hp = 1000;
            }
            foreach (var item in playerdict)
            {
                Console.WriteLine("键：" + item.Key + "\t值：" + item.Value.hp);
            }
            #endregion

            #region 委托
            MyDelegate myDelegate = new MyDelegate(PrintName);
            myDelegate("Pfolg");
            PrintName("哈利波特");
            //way2
            //MyDelegate myDelegate1 = PrintName;

            //function action
            Action action = Test;
            action();
            Action<string> action1 = PrintName;
            action1("你好");
            Action<int, string> action2 = Test;
            action2(99, "最大的两位数为");

            Func<int, int> func1 = Test1;//有参数+有返回值 参数在前，返回值在后
            int aaa = func1(1);
            Console.WriteLine(aaa);
            #endregion

            #region 多播委托
            Action act = Function;
            act += Function1;
            act+= Function2;
            act += Function3;
            act();
            act -= Function2;
            Console.WriteLine();
            act();
            #endregion

            #region 事件
            EventTest e=new EventTest();//发布器
            SubscribEvent s=new SubscribEvent("Tom");//订阅者  
            SubscribEvent s1=new SubscribEvent("Sam");
            e.changeNum += s.Print;
            
            e.Setvalue(2);
            e.Setvalue(5);

            e.changeNum += s1.Print;
            Console.Write("请输入一个字符：");
            string ss=Console.ReadLine();
            if (ss=="s")
            {
                e.Setvalue(0);
            }
            #endregion
            Console.ReadKey();
        }

    }
    #region 常量
    class hhh
    {
        public const int h = 360;//常量
        public const string path = "C:/Program Files";
        public hhh() { }
        #endregion

        #region 接口
        public interface IAnimal
        {
            //void MakeSound() { Console.WriteLine(); }//目标运行时不支持默认接口实现。
            void MakeSound();

            void Eat();
        }
        public class Dog : IAnimal
        {
            public void Eat()
            {
                //throw new NotImplementedException();
                Console.WriteLine("狗在吃饭");
            }

            public void MakeSound()
            {
                Console.WriteLine("bak");
            }
        }
        public class Cat : IAnimal
        {
            public void Eat()
            {
                throw new NotImplementedException();
            }

            public void MakeSound()
            {
                //throw new NotImplementedException();
                Console.WriteLine("喵");
            }
        }
        #endregion

        #region 多重继承
        public interface Imove
        {
            //int HP { get; set; }
            //int MP { get; set; }
            void Walk();
            void run();
        }
        public interface IAttack
        {
            void Attack();
            void SpecialAttack();
        }
        public interface ISkill
        {
            void Skill();
        }
        //多重继承 把类放到最前面
        public class Player : Character, Imove, IAttack, ISkill
        {
            //public int HP { get; set; }
            //public int MP { get; set; }

            public void Attack()
            {
                //throw new NotImplementedException();
            }

            public void run()
            {
                //throw new NotImplementedException();
            }

            public void Skill()
            {
                //throw new NotImplementedException();
            }

            public void SpecialAttack()
            {
                //throw new NotImplementedException();
            }

            public void Walk()
            {
                //throw new NotImplementedException();
            }
        }

        public class Character
        {
            public int hp;
            public int mp;
        }

        public struct Enemy : Imove, ISkill, IAttack
        {
            //public int HP { get => throw new NotImplementedException(); set => throw new NotImplementedException(); }
            //public int MP { get => throw new NotImplementedException(); set => throw new NotImplementedException(); }

            public void Attack()
            {
                throw new NotImplementedException();
            }

            public void run()
            {
                throw new NotImplementedException();
            }

            public void Skill()
            {
                throw new NotImplementedException();
            }

            public void SpecialAttack()
            {
                throw new NotImplementedException();
            }

            public void Walk()
            {
                throw new NotImplementedException();
            }
        }
        #endregion

        #region 泛型
        public class PrintData<T>
        {
            private T data;
            public T Data { get { return data; } }
            public void SetNumber(T value)
            {
                data = value;
            }
            public T GetNumber()
            {
                return data;
            }
        }
        #endregion

        #region 泛型方法与多个参数
        public static void PrintNumber<自定义变量名>(自定义变量名 num)
        {
            Console.WriteLine(typeof(自定义变量名));
        }
        public class A
        {
            public T Test<T>(T a)
            {
                return a;
            }
            public void Test<T, K, V>(T a, K b, V c)
            {
                Console.WriteLine(a);
                Console.WriteLine(b);
                Console.WriteLine(c);
            }
        }
        #endregion

        #region 委托
        public delegate void MyDelegate(string name);
        public static void PrintName(string name)
        {
            Console.WriteLine(name);
        }
        #endregion

        #region 类型强委托
        public static void Test()
        {
            Console.WriteLine("HelloWorld");
        }
        public static void Test(int a, string b)
        {
            Console.WriteLine(b + a);
        }
        public static int Test1(int a)
        {
            return a;
        }
        #endregion

        #region 多播委托
        public static void Function()
        {
            Console.WriteLine(0);
        }
        public static void Function1()
        {
            Console.WriteLine(1);
        }
        public static void Function2()
        {
            Console.WriteLine(2);
        }
        public static void Function3()
        {
            Console.WriteLine(3);
        }
    }
    #endregion

    #region 事件
    /// <summary>
    /// 发布器类
    /// </summary>
    public class EventTest
    {
        //首先需要一个数字
        private int value;

        public delegate void NumChangeHander();

        public event NumChangeHander changeNum;

        /// <summary>
        /// 数字发生改变调用的方法
        /// </summary>
        public void OnNumChanged()
        {
            changeNum();
        }
        /// <summary>
        /// 设置数字值
        /// </summary>
        /// <param name="n"></param>
        public void Setvalue(int n)
        {
            value = n;
            OnNumChanged();
        }
    }

    public class SubscribEvent
    {
        public string Player;
        public SubscribEvent(string player)
        {
            Player = player;
        }
        public SubscribEvent() { }

        public void Print()
        {
            Console.WriteLine("number changed "+Player+"收到");
            //Console.ReadKey();
        }
    }
    #endregion

}



#region namespace
namespace mySpace
    {
        namespace anamespace//命名空间之间可以互相嵌套
        {
            class aclass
            {
                public void func()
                {
                    Console.WriteLine("这是个方法");
                }
            }
        }
        namespace anothernamespace
        {
            class aclass
            {
                public void func()
                {
                    Console.WriteLine("一个方法");
                }
            }
        }
    }


#endregion

