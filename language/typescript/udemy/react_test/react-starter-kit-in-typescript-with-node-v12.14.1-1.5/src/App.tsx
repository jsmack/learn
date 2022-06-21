import React from 'react';


interface AppProps {
  message: string
}

// jsxフォーマット
//トランスファイル
// 引数を受け取るにはpropsで受け取る
//const App = (props: any) => {
// message以外は許容しないようにする
//  const App = ({ message } : {message: string}) => {

const App = ({message}: AppProps) => {
  //console.log(props);
  //const { message } = props;
  return <div>React Starter Kit in TypeScript {message} </div>;
};

export default App;
