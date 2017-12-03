export default function CompareValores(valores){
  
return valores.reduce((state,valor,index) =>{
    return [...state,...Combinacoes(valor,valores.slice(index+1,valores.length))]
  },[])
}
function Combinacoes(valor,vetor){

  return [valor,...vetor].reduce((state,dimensao,index)=>{
        let ref = [valor,...vetor].slice(0,index+1);
        console.log(index)
      return [...state, ...vetor.slice(index,vetor.length + 1).map((v,i) =>{
            return[...ref,v]
          })]
      return state;
  },[valor]);

}
