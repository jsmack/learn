import React from 'react';
import Counter from './Counter';
import CounterWithReducer from './CounterWithReducer';


interface AppProps {
  message?: string
  
}

// jsxフォーマット
//トランスファイル
// 引数を受け取るにはpropsで受け取る
//const App = (props: any) => {
// message以外は許容しないようにする
//  const App = ({ message } : {message: string}) => {

// const App = ({message}: AppProps) => {
//   //console.log(props);
//   //const { message } = props;
//   return <div>React Starter Kit in TypeScript {message} </div>;
// };

//アノテーション
// React.FunctionComponentは方引数を受け取れる
// messageの方引数は<AppProps>があるので不要
const App: React.FunctionComponent<AppProps> = ({message}) => {
  //console.log(props);
  //const { message } = props;
  //return <div>{message} </div>;

  return (
    <div>
        <Counter />
        <CounterWithReducer />
    </div>
  )
};

//messageのデフォルト値を設定
App.defaultProps = {
  message: 'stranger'
}
export default App;
