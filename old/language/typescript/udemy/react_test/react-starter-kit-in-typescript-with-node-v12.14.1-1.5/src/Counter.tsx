// usestateは状態管理(値保持)
//(alias) function useRef<T>(initialValue: T): MutableRefObject<T> (+2 overloads)
//import useRef
//(alias) function useEffect(effect: EffectCallback, deps?: DependencyList): void
//import useEffect
import React,{ useEffect, useRef, useState } from "react";

const Counter: React.FunctionComponent<{}> = () => {
  //const value = 0;
  const initialValue: any = 0;

  //ジェネリックでnumberをしているとほかがすべてnumberになる
  const [value, SetValue] = useState<number>(initialValue);

  const increment = () => {
    //SetValue(value + 1);
    //(parameter) previousState: number
    SetValue((previousState) => previousState + 1);
  };
  const decrement = () => {
    //SetValue(value - 1);
    SetValue((previousState) => previousState - 1);

  };

  const arenderTimes = useRef<number>(0);
  useEffect(() => {
    //console.log('done');
    arenderTimes.current = arenderTimes.current + 1;
  });

  // nullじゃないよ！ を nonnullassetionoperetor
  const ref = useRef<HTMLInputElement>(null!);
  
  const focusInput = () => {
 //   const current = ref.current;
 //   if ( current != null) ref.current?.focus();
 //   ref.current?.focus();
  ref.current.focus();
  };

  return (
    <div>
      <div>value: {value}</div>
      <button onClick={increment}>+1</button>
      <button onClick={decrement}>-1</button>
      <div>re-renderd {arenderTimes.current} times!</div>
      <input ref={ref} type="text"></input>
      <button onClick={focusInput}>click me!</button>
    </div>
  );
};

//Appkonnpo-nentokara 
//importできるようにexportをする
export default Counter;