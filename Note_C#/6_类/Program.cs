using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _6_类
{
    internal class Program
    {
        public static double pi = 3.141592654d;
        static void Main(string[] args)
        {
            GameManager.gameIsPaused = true;
            #region 深拷贝和浅拷贝
            Person LiHua = new Person();
            LiHua.Name = "李华";
            LiHua.age = 18;
            Person DaMing = new Person();
            DaMing.Name = "大明";
            DaMing.age = 20;
            //浅拷贝 对地址的引用 同一内存
            Person person = LiHua;
            Console.WriteLine(person.Equals(LiHua));
            //深拷贝 值相同但内存地址不同 如果要相同需要重写方法
            Person p = new Person();
            p.Name = LiHua.Name;
            p.age = LiHua.age;
            Console.WriteLine(p.Equals(LiHua));
            //深拷贝重写方法
            Person p2 = LiHua.Clone();
            Console.WriteLine(p2.Equals(LiHua));

            Person p3 = new Person(1);//out 这是一个重写的构造方法

            #endregion

            #region 属性
            //我们无法访问 hp 这个值
            Player ply1 = new Player();
            ply1.HP = 10;
            Console.WriteLine(ply1.HP);
            #endregion

            #region 静态类与静态成员
            Console.WriteLine(GameManager.gameIsPaused);

            Player ply2 = new Player();
            Console.WriteLine("两个玩家之间的距离为：" + calculateDistence(ply1, ply2));
            #endregion

            #region 继承
            Rectangle r1 = new Rectangle();
            r1.SetWidth(5);
            r1.SetHeight(5);
            Console.WriteLine("area=" + r1.GetArea());
            Console.WriteLine("id=" + r1.GetId());
            Rectangle r2 = new Rectangle(10, 10);//先调父类再调子类

            //方法重写
            Shape shape = new Shape();
            Rectangle r3 = new Rectangle();
            //Circle circle = new Circle();
            shape.PrintShape();
            r3.PrintShape();
            //circle.PrintShape();
            #endregion

            #region 多态
            PrintData.Print("你好");
            PrintData.Print(100);
            PrintData.Print((float)pi);

            //运算符多态
            Character c1 = new Character(100, 50, 40, "r1");
            Character c2 = new Character(10, 40, 100, "r2");
            Character c3 = new Character(10, 80, 60, "r3");
            Console.WriteLine("目前玩家的整体数据为：");
            Character newplayer = new Character();
            newplayer = c1 + c2 + c3;
            newplayer.show();
            #endregion

            #region 隐藏基类成员与阻止重写
            BaseClass bc1 = new BaseClass();
            bc1.DoWork();
            Console.WriteLine("bc1.workFiled = " + bc1.workFiled);

            SonClass sc1 = new SonClass();
            sc1.DoWork();
            Console.WriteLine("sc1.workFiled = " + sc1.workFiled);
            //这两个输出相差二
            #endregion

            #region 抽象类
            //CT cc=new CT();//无法创建抽象类型或接口“Program.CT”的实例
            #endregion

            #region 多态性与继承应用
            Father fa=new Father();
            fa.Draw();
            Son son = new Son();
            son.Draw();

            //父类声明子类实例化 向上转型
            Father person1=new Son();
            person1.Draw();//本质上是son

            ////子类声明父类实例化 向下转型
            //Son person2=(Son)new Father();//这种转换是不安全的
            ////无法将类型为“Father”的对象强制转换为类型“Son”。
            //person2.Draw();
            Son son1 = (Son)person1;
            son1.Draw();//本质上是son

            Console.WriteLine("\n定义 families 数组");
            Father[] families =
            {
                new Son(),
                new Daughter(),
            };
            foreach (Father f in families)
            {
                f.Draw();
            }

            //as 关键字 安全转化
            Son p1= new Father() as Son;
            if (p1 != null)
            {
                p1.Draw();
            }
            else
            {
                Console.WriteLine("转化失败");
            }
            //p1.Draw();//这里是直接报错了的
            #endregion
            //Console.WriteLine("pi="+pi);
            Console.ReadKey();
            GameManager.gameIsPaused = false;
        }

        #region 深拷贝和浅拷贝
        public class Person
        {
            public string Name;
            public int age;

            public Person() { }
            public Person(string name, int age)//构造函数 方法重写
            {
                this.Name = name;
                this.age = age;
            }
            public Person(int a)
            {
                Console.WriteLine("这是一个重写的构造方法");
            }
            public Person Clone()//深拷贝重写方法
            {
                return (Person)MemberwiseClone();
            }

        }
        #endregion

        #region 属性
        public class Player
        {
            private int hp;//private
            private int mp;
            //简写
            //public int HP { get; set; }


            //全写
            public int HP
            {

                get { return hp; }

                set
                {
                    hp = value;
                    GameManager.PauseGame();
                    Console.WriteLine(GameManager.gameIsPaused);
                    GameManager.continueGame();
                }
            }

            #region 指定无法设置
            //public int HP { get;private set; }
            #endregion

            #region 原始思路
            //            public int GetHPValue()
            //            {
            //return HP;
            //            }

            //            public void SetHPValue(int v)
            //            {
            //                HP = v;
            //            }
            //        }
            #endregion
        }
        #endregion

        #region 静态类与静态成员
        public static class GameManager
        {
            public static bool gameIsPaused { get; set; }

            public static void PauseGame()
            {
                GameManager.gameIsPaused = true;
            }
            public static void continueGame()
            {
                gameIsPaused = false;
            }
        }
        //静态方法
        public static float calculateDistence(Player p1, Player p2)
        {
            //一通计算
            return 3.14f;
        }
        #endregion

        #region 基类&派生类/父类&子类
        /// <summary>
        /// 基类
        /// </summary>
        class Shape
        {
            protected int width;
            protected int height;
            private int id;

            public virtual void PrintShape()//virtual 方法可以被调用，也可以被重写
            {
                Console.WriteLine("打印形状");
            }

            //基类的构造函数
            public Shape()
            {

            }
            public Shape(int width, int height)
            {
                this.width = width;
                this.height = height;
                Console.WriteLine("调用了父类的构造函数");
            }

            public void SetWidth(int w)
            {
                width = w;
            }
            public void SetHeight(int h)
            {
                height = h;
            }
            public void SetId(int i)
            {
                id = i;
            }
            public int GetId()
            {
                return id;
            }
        }
        /// <summary>
        /// 派生类
        /// </summary>
        class Rectangle : Shape
        {

            public override void PrintShape()
            {
                //base.PrintShape(); //完全重写
                Console.WriteLine("打印矩形");
            }
            //子类的构造函数
            public Rectangle(int w, int h) : base(w, h)
            {
                Console.WriteLine("调用了子类的构造函数");
            }
            public Rectangle() { }
            public int GetArea()
            {
                //继承自父类
                return width * height;
            }
        }
        class Circle : Shape
        {
            public override void PrintShape()
            {
                //base.PrintShape();
                Console.WriteLine("打印圆形");
            }
        }
        #endregion

        #region 多态 静态/动态
        /// <summary>
        /// 主要特点其实就是函数的参数不同
        /// </summary>
        class PrintData
        {
            public static void Print(int x)
            {
                Console.WriteLine("输出整形的 " + x);
            }
            public static void Print(string x)
            {
                Console.WriteLine("输出字符型的 " + x);
            }
            public static void Print(float x)
            {
                Console.WriteLine("输出浮点型的 " + x);
            }

        }
        //运算符重载 可以把加法变成减法
        class Character
        {
            public int hp;
            public int mp;
            public int at;
            public string name;
            public Character(int hp, int mp, int at, string name)
            {
                this.hp = hp;
                this.mp = mp;
                this.at = at;
                this.name = name;
            }
            public Character() { }

            public static Character operator +(Character a, Character b)
            {
                Character playerData = new Character();
                playerData.hp = a.hp + b.hp;
                playerData.mp = a.mp + b.mp;
                playerData.at = a.at + b.at;
                return playerData;
            }
            public void show()
            {
                Console.WriteLine("hp = " + hp);
                Console.WriteLine("mp = " + mp);
                Console.WriteLine("attackValue = " + at);

            }
        }

        class PlayerData//不重要的类
        {
            public int hp;
            public int mp;
            public int at;
            public string name;
        }
        #endregion

        #region 隐藏基类成员与阻止重写
        class BaseClass
        {
            public int workFiled = 0;
            public int workProperty
            {
                get { return 0; }
            }
            public void DoWork()
            {
                workFiled++;
            }
        }
        class SonClass : BaseClass
        {
            public new int workFiled = 1;
            public new int workProperty
            {
                get { return 1; }
            }
            public new void DoWork()
            {
                workFiled += 2;
            }
        }
        class A
        {
            public virtual void DoWork() { }
        }
        class B : A
        {
            public override void DoWork()
            {

            }
        }
        class C : B
        {
            //我们希望从此处开始之后，
            //以后的类就不能再使用这个方法重写
            public sealed override void DoWork() { }
        }
        class D : C
        {
            //那就重新定义一个方法
            public new void DoWork() { }//“Program.D.DoWork()”: 继承成员“Program.C.DoWork()”是密封的，无法进行重写
        }
        #endregion

        #region 抽象类
        //抽象类不能实例化，作为父类，抽象方法必须重写
        public class GameObject
        {
            public void Jump() { }
        }

        public abstract class CT:GameObject
        {
            public void Move()
            {
                Console.WriteLine("人物可以移动");
            }
            public abstract void Attack();//没有方法体
        }
        public class PY : CT
        {
            public override void Attack()
            {
                //throw new NotImplementedException();
                Console.WriteLine("玩家攻击");
            }

        }

        public class EY : CT
        {
            public override void Attack()
            {
                //throw new NotImplementedException();
                Console.WriteLine("敌人攻击");
            }
        }
        #endregion

        #region 多态性与继承应用
        public class Father
        {
            public int age;
            public string name;

            public virtual void Draw() 
            {
                Console.WriteLine("父亲的画画风格");
            }
        }

        public class Son:Father
        {
            public int money;
            public override void Draw()
            {
                //base.Draw();
                Console.WriteLine("儿子的画画风格");
            }

            public void PlayBall()
            {
                Console.WriteLine("儿咋会打球");
            }
        }
        public class Daughter:Father
        {
            public override void Draw()
            {
                //base.Draw();
                Console.WriteLine("女儿的画画风格");
            }

        }
        #endregion
    }
}
