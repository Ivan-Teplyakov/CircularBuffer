'''
Created on 9 January. 2019 y.
This module contains the ring buffer realization 

@author: Ivan
'''
import unittest
import ringBuffer

class TestRingBuffer(unittest.TestCase):
    
    """Creating new ring buffer with some predefined length, e.g. 5-element buffer""" 
    ringBuf = ringBuffer.RingBuffer(5)
    
    def test1WritingData(self):
        """writing data to ring buffer""" 
        TestRingBuffer.ringBuf.append(100)    
        referenceBuffer = [100,0,0,0,0]
        self.assertEqual(TestRingBuffer.ringBuf(), referenceBuffer)
    
    def test2WritingData(self):
        """writing data array to ring buffer""" 
        for element in range(1,20):
            TestRingBuffer.ringBuf.append(element)    
        referenceBuffer = [15,16,17,18,19]
        self.assertEqual(TestRingBuffer.ringBuf(), referenceBuffer)
        
    def test3RewritingData(self):
        """rewriting data to ring buffer""" 
        for element in range(1,3):
            TestRingBuffer.ringBuf.append(element*100)
        referenceBuffer = [100,200,17,18,19]
        self.assertEqual(TestRingBuffer.ringBuf.volume, referenceBuffer)    
    
    def test4GettingData(self):
        """Getting one data from ring buffer"""
        TestRingBuffer.ringBuf.get()
        referenceBuffer = [100,200,0,18,19]
        self.assertEqual(TestRingBuffer.ringBuf.volume, referenceBuffer)
    
    def test5GetingDatas(self):
        """Getting several data from ring buffer"""
        for iteration in range(1,4):
            TestRingBuffer.ringBuf.get()
        referenceBuffer = [0,200,0,0,0]
        self.assertEqual(TestRingBuffer.ringBuf.volume, referenceBuffer) 
    
    def test6WritingData(self):
        """writing data to ring buffer""" 
        TestRingBuffer.ringBuf.append(100)  
        TestRingBuffer.ringBuf.append(300)  
        referenceBuffer = [0,200,100,300,0]
        self.assertEqual(TestRingBuffer.ringBuf(), referenceBuffer)
    
    def test7Length(self):
        """Testing ring buffer length"""
        refenceLength = 5
        ringBufLength = len(TestRingBuffer.ringBuf)
        self.assertEqual(ringBufLength, refenceLength) 
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()