package com.azeefayzon

object FunctionalMatrixBasics {

  def main(args: Array[String]): Unit = {
    val testMatrixA = new ReferentiallyTransparentMatrix(Seq(Seq(1, 2), Seq(3, 4)))
    val testMatrixB = new ReferentiallyTransparentMatrix(Seq(Seq(1, 1), Seq(1, 1)))

    //adding matrices
    val added = testMatrixA.add(testMatrixB)
    println(added)

    //multiplying matrices
    val multiplied = testMatrixA.multiply(testMatrixB)
    println(multiplied)

    //transposing a matrix
    val transposed = testMatrixA.transpose()
    println(transposed)
  }

}
