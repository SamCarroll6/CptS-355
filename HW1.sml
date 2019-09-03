(*
1)
	A)
*)
fun inList (y, []) = false
      | inList (y, (x::rest)) = if x=y then true else inList (y, rest);

(*
1)
	B) The reason we get the type ''a as opposed to 'a is the 'a type would not work with the comparison x=y that I use,
	for this reason it must be the ''a type that allows for equality comparisons. 
*)

(*2)*)
fun removeDuplicates [] = []
      | removeDuplicates (x::rest) = if inList (x, rest) then removeDuplicates rest
                                     else [x] @ (removeDuplicates rest);
									
(*3)*)
fun listintersect [] L = []
      | listintersect (x::rest) L = if inList (x, L) then (listintersect rest L)@[x]
                                                    else listintersect rest L;
													
fun listIntersect ([], L) = []
	|listIntersect ((x::rest), L) = listintersect (removeDuplicates (x::rest)) (removeDuplicates L);


(*4)*)
fun range x y z = if ((y>=0 andalso x>=z) orelse (y<=0 andalso x<=z)) then []
				  else [x]@(range (x+y) y z);

(*5)*)
fun numbersToSum y [] = []
      | numbersToSum y (x::rest) = if (y-x)>0 then [x]@(numbersToSum (y-x) rest)
								   else [];
					
(*6)*)
fun replace y z [] = []
      | replace y z (x::rest) = if y=0 then [z]@rest
                                else [x]@(replace (y-1) z rest);

fun BufferL (n,[],L) = [L]
	  | BufferL(n,x::rest,L) = if length(L) = n then (L)::(BufferL(n,rest,[x]))
								else BufferL(n,rest,(x::L));
					
fun BufferR (n,[],L) = [rev(L)]
	  | BufferR(n,x::rest,L) = if length(L) = n then rev(L)::(BufferR(n,rest,[x]))
							   else BufferR(n,rest,(x::L));
							   
(*7)*)
fun groupNleft n [] = []
      | groupNleft n (x::rest) = rev(BufferL(n,rev(x::rest),[]));

	  
(*8)*)
fun groupNright n [] = []
	  | groupNright n (x::rest) = BufferR(n,(x::rest),[]);
								 

(*****************************************TESTS*********************************************)

(****************************************inList test *********************************************)

fun inList_test () = 
	  let 
		val inList1 = (inList (1, [1,10,2,9,3,8,4,7,5,6]) = true)
		val inList2 = (inList (6, [1,10,2,9,3,8,4,7,5,6]) = true)
		val inList3 = (inList (3, [1,10,2,9,3,8,4,7,5,6]) = true)
		val inList4 = (inList (15, [1,10,2,9,3,8,4,7,5,6]) = false)
	  in 
		print ("\n----------- \n inList: \n" ^
			  "Test 1: " ^ Bool.toString(inList1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(inList2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(inList3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(inList4) ^ "\n")
	  end;
inList_test();

(****************************** removeDuplicates test ****************************************)
  
fun removeDuplicates_test () = 
	  let 
		val removeDuplicates1 = (removeDuplicates([1,10,2,9,3,8,4,7,5,6]) = [1,10,2,9,3,8,4,7,5,6])
		val removeDuplicates2 = (removeDuplicates(["a", "A", "b", "B", "b"]) = ["a", "A", "B", "b"])
		val removeDuplicates3 = (removeDuplicates([1,10,4,9,3,3,4,7,5,6]) = [1,10,9,3,4,7,5,6])
		val removeDuplicates4 = (removeDuplicates([1,1,1,1,1,1,1,1,1,1]) = [1])
	  in 
		print ("\n----------- \n removeduplicates: \n" ^
			  "Test 1: " ^ Bool.toString(removeDuplicates1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(removeDuplicates2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(removeDuplicates3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(removeDuplicates4) ^ "\n")
	  end;	  
removeDuplicates_test();

(******************************** listIntersect test *****************************************)
  
fun listIntersect_test () = 
	  let 
		val listIntersect1 = (listIntersect ([1,2,3,4,5], [5,4,3,2,1]) = [5,4,3,2,1])
		val listIntersect2 = (listIntersect ([10,20,30,40,50], [20,20,10,10,10]) = [20,10])
		val listIntersect3 = (listIntersect ([1,2,3,4,5], [6,7,8,9]) = [])
		val listIntersect4 = (listIntersect (["a","b","c","d"], ["b","c","f","g"]) = ["c","b"])
	  in 
		print ("\n----------- \n listIntersect: \n" ^
			  "Test 1: " ^ Bool.toString(listIntersect1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(listIntersect2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(listIntersect3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(listIntersect4) ^ "\n")
	  end;	  
listIntersect_test();

(********************************** range Test ******************************************)
  
fun Range_test () = 
	  let 
		val range1 = (range 10 13 50 = [10,23,36,49])
		val range2 = (range 50 ~13 10 = [50,37,24,11])
		val range3 = (range 0 ~1 ~5 = [0,~1,~2,~3,~4])
		val range4 = (range 15 ~3 29 = [])
	  in 
		print ("\n----------- \n Range: \n" ^
			  "Test 1: " ^ Bool.toString(range1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(range2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(range3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(range4) ^ "\n")
	  end;	  
Range_test();

(******************************* numbersToSum Test *****************************************)
  
fun numbersToSum_test () = 
	  let 
		val numbersToSum1 = (numbersToSum ~100 [50,150,~10,15] = [])
		val numbersToSum2 = (numbersToSum 30 [20,9,~5,4,1,2] = [20,9,~5,4,1])
		val numbersToSum3 = (numbersToSum ~20 [~35,10,5,5,15,1,2,3] = [~35,10])
		val numbersToSum4 = (numbersToSum 55 [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] = [1,2,3,4,5,6,7,8,9])
	  in 
		print ("\n----------- \n NumbersToSum: \n" ^
			  "Test 1: " ^ Bool.toString(numbersToSum1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(numbersToSum2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(numbersToSum3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(numbersToSum4) ^ "\n")
	  end;	  
numbersToSum_test();

(********************************* replace Test ******************************************)
  
fun replace_test () = 
	  let 
		val replace1 = (replace 5 30 [0,1,2,3] = [0,1,2,3])
		val replace2 = (replace ~1 14 [0,1,2,3,4,5] = [0,1,2,3,4,5])
		val replace3 = (replace 3 1000 [10,10,10,0] = [10,10,10,1000])
		val replace4 = (replace 5 "g" ["a","b","c","d","e","f","g"] = ["a","b","c","d","e","g","g"])
	  in 
		print ("\n----------- \n replace: \n" ^
			  "Test 1: " ^ Bool.toString(replace1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(replace2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(replace3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(replace4) ^ "\n")
	  end;	  
replace_test();	

(************************************ GroupNleft Test ******************************************)
  
fun groupNleft_test () = 
	  let 
		val groupNleft1 = (groupNleft 2 [50,40,30,20,10,0] = [[50,40],[30,20],[10,0]])
		val groupNleft2 = (groupNleft 3 [0,1,2,3,4,5,6,7,8,9] = [[0],[1,2,3],[4,5,6],[7,8,9]])
		val groupNleft3 = (groupNleft ~1 [1,2,3,4,5] = [[1,2,3,4,5]])
		val groupNleft4 = (groupNleft 5 [10,20,30,40] = [[10,20,30,40]])
	  in 
		print ("\n----------- \n groupNleft: \n" ^
			  "Test 1: " ^ Bool.toString(groupNleft1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(groupNleft2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(groupNleft3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(groupNleft4) ^ "\n")
	  end;	  
groupNleft_test();

(************************************ GroupNright Test ******************************************)
  
fun groupNright_test () = 
	  let 
		val groupNright1 = (groupNright 2 [50,40,30,20,10,0] = [[50,40],[30,20],[10,0]])
		val groupNright2 = (groupNright 3 [0,1,2,3,4,5,6,7,8,9] = [[0,1,2],[3,4,5],[6,7,8],[9]])
		val groupNright3 = (groupNright ~1 [1,2,3,4,5] = [[1,2,3,4,5]])
		val groupNright4 = (groupNright 5 [10,20,30,40] = [[10,20,30,40]])
	  in 
		print ("\n----------- \n groupNright: \n" ^
			  "Test 1: " ^ Bool.toString(groupNright1) ^ "\n" ^
			  "Test 2: " ^ Bool.toString(groupNright2) ^ "\n" ^
			  "Test 3: " ^ Bool.toString(groupNright3) ^ "\n" ^
			  "Test 4: " ^ Bool.toString(groupNright4) ^ "\n")
	  end;	  
groupNright_test();
			   