import CompareValores from '../component/compareValores';

describe('Compare Valores', () => {
   test('[A] | A ', () => {
     const expected = [1];
     expect(CompareValores([1])).toEqual(expected);
   });
  test('[A,B] | A , B, AB', () => {
    const expected = [1,[1,2],2]
    expect(CompareValores([1,2])).toEqual(expected);
  });
  
   test('[A,B,C] | A , B, C, AB, AC, BC, ABC', () => {
     const expected = 
        [1, 
        [1, 2], 
        [1, 3],
        [1,2,3], 
        2, 
        [2, 3], 
        3];
     expect(CompareValores([1,2,3])).toEqual(expected);
   });

   test('[A,B,C,D] | ', () => {
    const expected = 
       [1, 
       [1, 2], 
       [1, 3],
       [1, 4],
       [1,2,3],
       [1,2,4],
       [1,3,4], 
       2, 
       [2, 3],
       [2, 4], 
       3,
        [3,4],
        4
      ];
    expect(CompareValores([1,2,3,4])).toEqual(expected);
  });
});
