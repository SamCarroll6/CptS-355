(*	Part 1 Helper Functions  *)
fun inList (n,[]) = false
| inList(n,x::rest) = if n=x then true else inList(n,rest);
fun removeDuplicates [] = []
| removeDuplicates (x::rest) = if inList(x,rest) then (removeDuplicates rest)
							   else x::(removeDuplicates rest);
(*****************************)

(*
	1)
	A)
*)

fun CILhelp [] z count = 0
| CILhelp (x::rest) z count = if x = z then CILhelp rest z count+1 
							  else CILhelp rest z count;

fun countInList L z = CILhelp L z 0;

(*
	B)
*)

fun zipTail M L = if (null(M) orelse null(L)) then [] else
let
fun aux (x::rest,y::Rest,acc) =
if 
(null(rest) orelse null(Rest)) 
then 
rev((x,y)::acc) 
else  
aux(rest, Rest, (x,y)::acc)
in
aux(M,L,[]) 
end;

(*
	C)
*)

fun histogram L = (removeDuplicates (zipTail L (map (fn x => (countInList (L) x)) (L))));

(*  Part 2 Helper Functions	 *)
fun fold f base [] = base
| fold f base (x::rest) = f x (fold f base rest);
fun addup x y = x+y;
fun sum L = fold addup 0 L;
datatype 'a Option = NONE | SOME of 'a;
fun OPTamount(NONE) = 0 | OPTamount(SOME(value)) = value;
fun addupOP x y = SOME((OPTamount(x)) + (OPTamount(y)));
fun sumOP L = fold addupOP NONE L;
(*****************************)

(*
	2)
	A)
*)

fun deepSum L = fold addup 0 (map sum L);

(*
	B)
*)

fun deepSumOption L = let
val m1 = fold addupOP NONE (map sumOP L)
in
if (OPTamount(m1)) = 0 then NONE else m1
end;

(*  Part 3 Helper Functions	 *)
fun f1 (x,y) = x;
fun f2 (x,y) = y;
(*****************************)

(*
	3)
*)

fun unzip L = (map f1 L)::[(map f2 L)];

(*
	4)
	A)
*)

datatype either = ImAString of string | ImAnInt of int;

(*
	B)
*)

datatype eitherTree = eLEAF of either | eINTERIOR of (either*eitherTree*eitherTree);

(*  Part 4 Helper Functions	 *)
fun eitherVal (ImAString(v1)) = false | eitherVal (v2) = true; 
fun eTreeVal (eLEAF(v1)) = false | eTreeVal (v2) = true;
fun eitherAmountS (ImAString(v1)) =  v1;
fun eitherAmountI (ImAnInt(v1)) = v1;
fun eitherTreeA (eLEAF(v1)) = v1; 
(*****************************)

(*
	C)
*)

fun eitherSearch (eLEAF(v1)) y = if (eitherVal v1) = true andalso (eitherAmountI v1 = y) then true else false
| eitherSearch (eINTERIOR(v2,t1,t2)) y = if (eitherVal v2) = true andalso (eitherAmountI v2 = y) then true else (eitherSearch t1 y) orelse (eitherSearch t2 y);

(*
	D)
*)
fun eitherTest() = 
let 
val s1 = eLEAF(ImAString("355"))
val i1 = eLEAF(ImAnInt(15))
val i2 = eLEAF(ImAnInt(19))
val i3 = eLEAF(ImAnInt(40))
val i4 = eLEAF(ImAnInt(3))
val i5 = eLEAF(ImAnInt(7))
val i6 = eLEAF(ImAnInt(8))
val i7 = eLEAF(ImAnInt(10)) 
val s2 = eINTERIOR(ImAString("There"),s1,i1)
val s3 = eINTERIOR(ImAnInt(13),i2,i3)
val s4 = eINTERIOR(ImAString("CPTS"),i4,i5)
val s5 = eINTERIOR(ImAnInt(355),i6,i7)
val s6 = eINTERIOR(ImAnInt(5),s2,s3)
val s7 = eINTERIOR(ImAString("Something"),s4,s5)
val tree = eitherSearch (eINTERIOR(ImAString("Hello"),s6,s7)) 100
in 
if tree = false then 
	print ( "******************************************EITHERTESTS WITH CUSTOM TREE******************************************" ^ "\n" ^
	"eitherTest with unlisted value:" ^ "\n" ^
	"\n" ^ "Test 1: " ^ Bool.toString(tree) ^ "\n")
else 
	print ( "******************************************EITHERTESTS WITH CUSTOM TREE******************************************" ^ "\n" ^
	"eitherTest with listed value:" ^ "\n" ^
	"\n" ^ "Test 1: " ^ Bool.toString(tree) ^ "\n")
end;

(*  Part 5 Helper Functions	 *)
datatype 'a Tree = LEAF of 'a | NODE of ('a Tree) * ('a Tree);
datatype 'a myTree = myLEAF of 'a | myNODE of 'a*'a*('a myTree)*('a myTree);
(*****************************)

(*
	5)
	A)
*)

fun findMin (LEAF(v1)) = v1
| findMin (NODE(t1,t2)) = if findMin t1 < findMin t2 then findMin t1 else findMin t2;

fun findMax (LEAF(v1)) = v1
| findMax (NODE(t1,t2)) = if findMax t1 > findMax t2 then findMax t1 else findMax t2;

(*
	B)
*)

fun minmaxTree (LEAF(v1)) = myLEAF(v1)
| minmaxTree (NODE(t1,t2)) = myNODE(findMin (NODE(t1,t2)), findMax (NODE(t1,t2)), minmaxTree (t1), minmaxTree (t2));

(*
	C) 
*)

fun minmaxTests() = 
let
val i1 = LEAF(2)
val i2 = LEAF(12)
val i3 = LEAF(3)
val i4 = LEAF(15)
val i5 = LEAF(19)
val n1 = NODE(i1,i2)
val n2 = NODE(n1,i3)
val n3 = NODE(i4,i5)
val tree = NODE(n2,n3)
val tree1 = (minmaxTree tree = myNODE(2,19,myNODE (2,12,myNODE (2,12,myLEAF (2),myLEAF(12)),myLEAF (3)),myNODE (15,19,myLEAF (15),myLEAF (19))));
val i1 = LEAF(15)
val i2 = LEAF(6)
val i3 = LEAF(7)
val i4 = LEAF(4)
val i5 = LEAF(2)
val i6 = LEAF(5)
val i7 = LEAF(3)
val i8 = LEAF(13)
val n1 = NODE(i1,i2)
val n2 = NODE(n1,i3)
val n3 = NODE(n2,i4)
val n4 = NODE(i5,i6)
val n5 = NODE(i7,i8)
val n6 = NODE(n4,n5)
val tree = NODE(n3,n6)
val tree2 = (minmaxTree tree = myNODE(2,15, myNODE(4,15,myNODE (6,15,myNODE (6,15,myLEAF(15),myLEAF(6)),myLEAF(7)), myLEAF(4)), myNODE(2,13,myNODE(2,5,myLEAF(2),myLEAF(5)),myNODE(3,13,myLEAF(3),myLEAF(13))))) 

in 
	print ( "*******************************MINMAXTREE TESTS WITH CUSTOM TREES********************************" ^ "\n"
		  ^ "minmaxTree Test 1: " ^ Bool.toString(tree1) ^ "\n"
		  ^ "minmaxTree Test 2: " ^ Bool.toString(tree2) ^ "\n")
	
end;

(*****************************#1-3TEST CASES AND CALLS FOR ABOVE TEST CASES*****************************)

(**************************************** countInList test *********************************************)

fun countInList_test () = 
	  let 
		val countInList1 = (countInList [1,1,1,1,1,1,55,143,1,1,13] 1 = 8)
		val countInList2 = (countInList ["a", "A", "b", "B", "b"] "b" = 2)
		val countInList3 = (countInList [true,true,true,true] false = 0)
		val countInList4 = (countInList ["0","0","1","15","0","12"] "0" = 3)
	  in 
		print ("\n----------- \n countInList: \n" ^
			  "Test 1: " ^ Bool.toString(countInList1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(countInList2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(countInList3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(countInList4) ^ "\n")
	  end;	  

(**************************************** zipTail test *********************************************)
fun zipTail_test () = 
	  let 
		val zipTail1 = (zipTail ["I","Am","Awesome"] [true,true,true] = [("I",true),("Am",true),("Awesome",true)])
		val zipTail2 = (zipTail [3,4,5,2,5] [1,1,9,6,3] = [(3,1),(4,1),(5,9),(2,6),(5,3)])
		val zipTail3 = (zipTail [15,25,34,2,3,4] [] = [])
		val zipTail4 = (zipTail [] [5,3,54,3,2,4,2,43] = [])
	  in 
		print ("\n----------- \n zipTail: \n" ^
			  "Test 1: " ^ Bool.toString(zipTail1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(zipTail2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(zipTail3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(zipTail4) ^ "\n")
	  end;	 
	  
(**************************************** histogram test *********************************************)
fun histogram_test () = 
	  let 
		val histogram1 = (histogram [5,5,5,5,5,15,1,2,2,3,3,3,4,4,4,4] = [(5,5),(15,1),(1,1),(2,2),(3,3),(4,4)])
		val histogram2 = (histogram ["a", "A", "b", "B", "b"] = [("a",1),("A",1),("B",1),("b",2)])
		val histogram3 = (histogram [(1,1),(2,2),(1,1),(2,2),(3,3)] = [((1,1),2),((2,2),2),((3,3),1)])
		val histogram4 = (histogram [] = [])
	  in 
		print ("\n----------- \n histogram: \n" ^
			  "Test 1: " ^ Bool.toString(histogram1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(histogram2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(histogram3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(histogram4) ^ "\n")
	  end;	

(**************************************** deepSum test *********************************************)
fun deepSum_test () = 
	  let 
		val deepSum1 = (deepSum [[5,5,5,5,5],[15],[1,2],[2,3,3,3,4],[4,4,4]] = 70)
		val deepSum2 = (deepSum [[20],[10,10],[5,5,5,5]] = 60)
		val deepSum3 = (deepSum [[42,24,12],[78]] = 156)
		val deepSum4 = (deepSum [] = 0)
	  in 
		print ("\n----------- \n deepSum: \n" ^
			  "Test 1: " ^ Bool.toString(deepSum1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(deepSum2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(deepSum3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(deepSum4) ^ "\n")
	  end;	

(**************************************** deepSumOption test *********************************************)
fun deepSumOption_test () = 
	  let 
		val deepSumOption1 = (deepSumOption [[SOME(5),SOME(5),SOME(5),SOME(5),SOME(5),NONE],[SOME(15),NONE],[SOME(1),SOME(2),NONE],[SOME(2),SOME(3),SOME(3),SOME(3),SOME(4),NONE],[SOME(4),SOME(4),SOME(4)]] = SOME 70)
		val deepSumOption2 = (deepSumOption [[NONE],[NONE],[NONE],[SOME(1)]] = SOME(1))
		val deepSumOption3 = (deepSumOption [[SOME(0),SOME(0),SOME(0)]] = NONE)
		val deepSumOption4 = (deepSumOption [[NONE]] = NONE)
	  in 
		print ("\n----------- \n deepSumOption: \n" ^
			  "Test 1: " ^ Bool.toString(deepSumOption1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(deepSumOption2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(deepSumOption3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(deepSumOption4) ^ "\n")
	  end;	

(**************************************** unzip test *********************************************)
fun unzip_test () = 
	  let 
		val unzip1 = (unzip [(1,4),(2,5),(3,6)] = [[1,2,3],[4,5,6]])
		val unzip2 = (unzip [(3,1),(4,1),(5,9),(2,6),(5,3)] = [[3,4,5,2,5],[1,1,9,6,3]])
		val unzip3 = (unzip [(6,5),(4,3),(2,1)]  = [[6,4,2],[5,3,1]])
		val unzip4 = (unzip [("1","a"),("5","b"),("8","c")] = [["1","5","8"],["a","b","c"]])
	  in 
		print ("\n----------- \n unzip: \n" ^
			  "Test 1: " ^ Bool.toString(unzip1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(unzip2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(unzip3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(unzip4) ^ "\n")
	  end;	

(**************************************** findMin test *********************************************)
fun findMin_test () = 
	  let 
		val findMin1 = (findMin (NODE(LEAF(10),LEAF(4))) = 4)
		val findMin2 = (findMin (NODE(NODE(LEAF(1),LEAF(15)),LEAF(4))) = 1)
		val findMin3 = (findMin (NODE(LEAF(10),NODE(LEAF(1),LEAF(45)))) = 1)
		val findMin4 = (findMin (NODE(NODE(NODE(LEAF(5),LEAF(29)),NODE(LEAF(80),NODE(LEAF(15),LEAF(18)))),NODE(LEAF(2),LEAF(90)))) = 2)
	  in 
		print ("\n----------- \n findMin: \n" ^
			  "Test 1: " ^ Bool.toString(findMin1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(findMin2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(findMin3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(findMin4) ^ "\n")
	  end;	

(**************************************** findMax test *********************************************)
fun findMax_test () = 
	  let 
		val findMax1 = (findMax (NODE(LEAF(10),LEAF(4))) = 10)
		val findMax2 = (findMax (NODE(NODE(LEAF(1),LEAF(15)),LEAF(4))) = 15)
		val findMax3 = (findMax (NODE(LEAF(10),NODE(LEAF(1),LEAF(45)))) = 45)
		val findMax4 = (findMax (NODE(NODE(NODE(LEAF(5),LEAF(29)),NODE(LEAF(80),NODE(LEAF(15),LEAF(18)))),NODE(LEAF(2),LEAF(90)))) = 90)
	  in 
		print ("\n----------- \n findMax: \n" ^
			  "Test 1: " ^ Bool.toString(findMax1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(findMax2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(findMax3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(findMax4) ^ "\n")
	  end;	
	  
countInList_test();
zipTail_test();
histogram_test();
deepSum_test();
deepSumOption_test();
unzip_test();
findMin_test();
findMax_test();
eitherTest();
minmaxTests();
