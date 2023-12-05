open Base

(* Define a split function *)
let split_by_char ch str =
  String.split_on_chars ~on:[ch] str

(* Read the file *)
let file =
  let f = In_channel.create "day4input.txt" in
  let content = In_channel.input_all f in
  In_channel.close f;
  content

(* Process cards *)
let cards =
  file
  |> String.split_lines
  |> List.map (fun line ->
      let parts = split_by_char '|' line in
      let card1 = parts.(0) |> String.strip |> split_by_char ' ' |> List.drop 2 |> List.map ~f:Int.of_string |> Int.Set.of_list in
      let card2 = parts.(1) |> String.strip |> split_by_char ' ' |> List.map ~f:Int.of_string |> Int.Set.of_list in
      [card1; card2]
    )

(* Calculate intersection and total *)
let winning =
  cards
  |> List.map (fun card -> Set.inter (List.nth_exn card 0) (List.nth_exn card 1)))

let total =
  winning
  |> List.map (fun card -> int_of_float (2. ** float_of_int (Set.length card - 1)))
  |> List.fold_left (+) 0

(* Calculate points *)
let copies = Array.create ~len:(List.length cards) 1 in
let points = Array.create ~len:(List.length cards) 0 in
for game = 0 to List.length cards - 1 do
  let rec distribute_points game =
    if copies.(game) > 0 then (
      let winning_game = Set.to_list (List.nth_exn winning game) in
      List.iteri winning_game ~f:(fun i _ -> copies.(game + i + 1) <- copies.(game + i + 1) + 1);
      points.(game) <- points.(game) + 1;
      copies.(game) <- copies.(game) - 1;
      distribute_points game
    )
  in
  distribute_points game
done

(* Calculate the total points *)
let total_points = Array.fold_left (+) 0 points

(* Print results *)
let () =
  print_endline (string_of_int total);
  print_endline (string_of_int total_points)
