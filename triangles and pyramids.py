{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "5acdbe86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "*\n",
      "**\n",
      "***\n",
      "****\n",
      "*****\n",
      "******\n",
      "*******\n",
      "********\n",
      "*********\n",
      "**********\n",
      "***********\n",
      "************\n"
     ]
    }
   ],
   "source": [
    "x=int(input(\"enter the number of rows\"))\n",
    "for i in range(0,x):\n",
    "    for j in range(0,i+1):\n",
    "        print(\"*\",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "07c95d4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "+\n",
      "++\n",
      "+++\n",
      "++++\n",
      "+++++\n",
      "++++++\n",
      "+++++++\n",
      "++++++++\n",
      "+++++++++\n",
      "++++++++++\n",
      "+++++++++++\n",
      "++++++++++++\n"
     ]
    }
   ],
   "source": [
    "x=int(input(\"enter the number of rows\"))\n",
    "for i in range (0,x):\n",
    "    for j in range(0,i+1):\n",
    "        print(\"+\",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "147822af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "&\n",
      "&&\n",
      "&&&\n",
      "&&&&\n",
      "&&&&&\n",
      "&&&&&&\n",
      "&&&&&&&\n",
      "&&&&&&&&\n",
      "&&&&&&&&&\n",
      "&&&&&&&&&&\n",
      "&&&&&&&&&&&\n",
      "&&&&&&&&&&&&\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "for i in range(0,a):\n",
    "    for j in range(0,i+1):\n",
    "        print(\"&\",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "ea4be0a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "*\n",
      "**\n",
      "***\n",
      "****\n",
      "*****\n",
      "******\n",
      "*******\n",
      "********\n",
      "*********\n",
      "**********\n",
      "***********\n",
      "************\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "k=2*a-a\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\"\")\n",
    "    k=k-2\n",
    "    for j in range (0,i+1):\n",
    "        print(\"*\",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2cef6a4",
   "metadata": {},
   "source": [
    "rows = int(input(\"Enter the number of rows:\"))  \n",
    "k = 2 * rows - 2  # It is used for number of spaces  \n",
    "for i in range(0, rows):  \n",
    "    for j in range(0, k):  \n",
    "        print(end=\" \")  \n",
    "    k = k - 2   # decrement k value after each iteration  \n",
    "    for j in range(0, i + 1):  \n",
    "        print(\"* \", end=\"\")  # printing star  \n",
    "    print(\"\")  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "c44cff90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "                      * \n",
      "                    * * \n",
      "                  * * * \n",
      "                * * * * \n",
      "              * * * * * \n",
      "            * * * * * * \n",
      "          * * * * * * * \n",
      "        * * * * * * * * \n",
      "      * * * * * * * * * \n",
      "    * * * * * * * * * * \n",
      "  * * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"enter the number of rows\"))\n",
    "k = a * 2 - 2\n",
    "for i in range (0 , a):\n",
    "    for  j in range (0 , k):\n",
    "        print(end=\" \")\n",
    "    k = k - 2\n",
    "    for j in range (0 , i + 1):\n",
    "        print(\"* \", end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "5ce782f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "enter the number of rows12\n",
      "* \n",
      "* * \n",
      "* * * \n",
      "* * * * \n",
      "* * * * * \n",
      "* * * * * * \n",
      "* * * * * * * \n",
      "* * * * * * * * \n",
      "* * * * * * * * * \n",
      "* * * * * * * * * * \n",
      "* * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n",
      "                      * \n",
      "                    * * \n",
      "                  * * * \n",
      "                * * * * \n",
      "              * * * * * \n",
      "            * * * * * * \n",
      "          * * * * * * * \n",
      "        * * * * * * * * \n",
      "      * * * * * * * * * \n",
      "    * * * * * * * * * * \n",
      "  * * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "b=int(input(\"enter the number of rows\"))\n",
    "for i in range (0,a):\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "\n",
    "k = b * 2 - 2\n",
    "for x in range(0 , b):\n",
    "    for y in range(0 , k):\n",
    "        print (end=\" \")\n",
    "    k = k - 2\n",
    "    for y  in range(0, x + 1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "b2c7c83f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "enter the number of rows :12\n",
      "* \n",
      "* * \n",
      "* * * \n",
      "* * * * \n",
      "* * * * * \n",
      "* * * * * * \n",
      "* * * * * * * \n",
      "* * * * * * * * \n",
      "* * * * * * * * * \n",
      "* * * * * * * * * * \n",
      "* * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n",
      "                      * \n",
      "                    * * \n",
      "                  * * * \n",
      "                * * * * \n",
      "              * * * * * \n",
      "            * * * * * * \n",
      "          * * * * * * * \n",
      "        * * * * * * * * \n",
      "      * * * * * * * * * \n",
      "    * * * * * * * * * * \n",
      "  * * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n"
     ]
    }
   ],
   "source": [
    "x=int(input(\"enter the number of rows :\"))\n",
    "y=int(input(\"enter the number of rows :\"))\n",
    "for i in range(0, x):\n",
    "    for j in range (0, i+1):\n",
    "        print(\"* \", end=\"\")\n",
    "    print()\n",
    "    \n",
    "k=y * 2 - 2\n",
    "for a in range(0 , y):\n",
    "    for b in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for b in range(0,a+1):\n",
    "        print(\"* \", end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "85cc6dda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "* \n",
      "* * \n",
      "* * * \n",
      "* * * * \n",
      "* * * * * \n",
      "* * * * * * \n",
      "* * * * * * * \n",
      "* * * * * * * * \n",
      "* * * * * * * * * \n",
      "* * * * * * * * * * \n",
      "* * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n",
      "                      * \n",
      "                    * * \n",
      "                  * * * \n",
      "                * * * * \n",
      "              * * * * * \n",
      "            * * * * * * \n",
      "          * * * * * * * \n",
      "        * * * * * * * * \n",
      "      * * * * * * * * * \n",
      "    * * * * * * * * * * \n",
      "  * * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n",
      "                      *   \n",
      "                    *   *   \n",
      "                  *   *   *   \n",
      "                *   *   *   *   \n",
      "              *   *   *   *   *   \n",
      "            *   *   *   *   *   *   \n",
      "          *   *   *   *   *   *   *   \n",
      "        *   *   *   *   *   *   *   *   \n",
      "      *   *   *   *   *   *   *   *   *   \n",
      "    *   *   *   *   *   *   *   *   *   *   \n",
      "  *   *   *   *   *   *   *   *   *   *   *   \n",
      "*   *   *   *   *   *   *   *   *   *   *   *   \n",
      "s\n",
      "su\n",
      "sup\n",
      "supe\n",
      "super\n",
      "super \n",
      "super s\n",
      "super st\n",
      "super sta\n",
      "super star\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(0,a):                                \n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \", end=\"\")\n",
    "    print()\n",
    "    \n",
    "k=a*2-2\n",
    "for i in range(0, a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0, k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range (0,i+1):\n",
    "        print(\"*  \",end=\" \")\n",
    "    print()\n",
    "    \n",
    "c=\"super star\"\n",
    "d=list(c)\n",
    "e=\"\"\n",
    "for g in d:\n",
    "    e=e+g\n",
    "    print(e)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34cc0f4f",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "3847ddc9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  \n",
      "*  *  \n",
      "*  \n",
      "\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "for i in range(a+1,0,-1):\n",
    "    for j in range(0,i-1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "c0912acb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  \n",
      "*  *  \n",
      "*  \n",
      "\n",
      "*  \n",
      "*  *  \n",
      "*  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  \n",
      "*  *  \n",
      "*  \n",
      "\n",
      "*  \n",
      "*  *  \n",
      "*  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "for i in range(a+1,0,-1):\n",
    "    for j in range(0,i-1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()\n",
    "for i in range(0,a):\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()\n",
    "for i in range(a+1,0,-1):\n",
    "    for j in range(0,i-1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()\n",
    "for i in range(0,a):\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "f17578b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "                      *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                       *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                        *  *  *  *  *  *  *  *  *  *  *  \n",
      "                         *  *  *  *  *  *  *  *  *  *  \n",
      "                          *  *  *  *  *  *  *  *  *  \n",
      "                           *  *  *  *  *  *  *  *  \n",
      "                            *  *  *  *  *  *  *  \n",
      "                             *  *  *  *  *  *  \n",
      "                              *  *  *  *  *  \n",
      "                               *  *  *  *  \n",
      "                                *  *  *  \n",
      "                                 *  *  \n",
      "                                  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in  range(a,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "aff9c0d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "                      *   \n",
      "                    *   *   \n",
      "                  *   *   *   \n",
      "                *   *   *   *   \n",
      "              *   *   *   *   *   \n",
      "            *   *   *   *   *   *   \n",
      "          *   *   *   *   *   *   *   \n",
      "        *   *   *   *   *   *   *   *   \n",
      "      *   *   *   *   *   *   *   *   *   \n",
      "    *   *   *   *   *   *   *   *   *   *   \n",
      "  *   *   *   *   *   *   *   *   *   *   *   \n",
      "*   *   *   *   *   *   *   *   *   *   *   *   \n",
      "                      *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                       *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                        *  *  *  *  *  *  *  *  *  *  *  \n",
      "                         *  *  *  *  *  *  *  *  *  *  \n",
      "                          *  *  *  *  *  *  *  *  *  \n",
      "                           *  *  *  *  *  *  *  *  \n",
      "                            *  *  *  *  *  *  *  \n",
      "                             *  *  *  *  *  *  \n",
      "                              *  *  *  *  *  \n",
      "                               *  *  *  *  \n",
      "                                *  *  *  \n",
      "                                 *  *  \n",
      "                                  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"  \")\n",
    "    print()\n",
    "k=a*2-2\n",
    "for i in range(a,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "f1f9a9f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "                      *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                       *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                        *  *  *  *  *  *  *  *  *  *  *  \n",
      "                         *  *  *  *  *  *  *  *  *  *  \n",
      "                          *  *  *  *  *  *  *  *  *  \n",
      "                           *  *  *  *  *  *  *  *  \n",
      "                            *  *  *  *  *  *  *  \n",
      "                             *  *  *  *  *  *  \n",
      "                              *  *  *  *  *  \n",
      "                               *  *  *  *  \n",
      "                                *  *  *  \n",
      "                                 *  *  \n",
      "                                  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "k=a*2-2\n",
    "for i in range(a,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "80ba6ec2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  \n",
      "*  *  \n",
      "*  \n",
      "\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "for i in range(a+1,0,-1):\n",
    "    for j in range(0,i-1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "aea76651",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "                      *   \n",
      "                     *   *   \n",
      "                    *   *   *   \n",
      "                   *   *   *   *   \n",
      "                  *   *   *   *   *   \n",
      "                 *   *   *   *   *   *   \n",
      "                *   *   *   *   *   *   *   \n",
      "               *   *   *   *   *   *   *   *   \n",
      "              *   *   *   *   *   *   *   *   *   \n",
      "             *   *   *   *   *   *   *   *   *   *   \n",
      "            *   *   *   *   *   *   *   *   *   *   *   \n",
      "           *   *   *   *   *   *   *   *   *   *   *   *   \n",
      "          *   *   *   *   *   *   *   *   *   *   *   *   *   \n",
      "           *   *   *   *   *   *   *   *   *   *   *   *   \n",
      "            *   *   *   *   *   *   *   *   *   *   *   \n",
      "             *   *   *   *   *   *   *   *   *   *   \n",
      "              *   *   *   *   *   *   *   *   *   \n",
      "               *   *   *   *   *   *   *   *   \n",
      "                *   *   *   *   *   *   *   \n",
      "                 *   *   *   *   *   *   \n",
      "                  *   *   *   *   *   \n",
      "                   *   *   *   *   \n",
      "                    *   *   *   \n",
      "                     *   *   \n",
      "                      *   \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"  \")\n",
    "    print(\"\")\n",
    "k=a-2\n",
    "for i in range(a,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"*  \",end=\" \")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "426533da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "                      * \n",
      "                     * * \n",
      "                    * * * \n",
      "                   * * * * \n",
      "                  * * * * * \n",
      "                 * * * * * * \n",
      "                * * * * * * * \n",
      "               * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n",
      "          * * * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "               * * * * * * * * \n",
      "                * * * * * * * \n",
      "                 * * * * * * \n",
      "                  * * * * * \n",
      "                   * * * * \n",
      "                    * * * \n",
      "                     * * \n",
      "                      * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "k=a-2\n",
    "for i in range(a,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "1dec1632",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "          * * * * * * * * * * * * * \n",
      "                      * * * * * * * * * * * * \n",
      "                      * * * * * * * * * * * \n",
      "                      * * * * * * * * * * \n",
      "                      * * * * * * * * * \n",
      "                      * * * * * * * * \n",
      "                      * * * * * * * \n",
      "                      * * * * * * \n",
      "                      * * * * * \n",
      "                      * * * * \n",
      "                      * * * \n",
      "                      * * \n",
      "                      * \n",
      "                      *  \n",
      "                     *  *  \n",
      "                    *  *  *  \n",
      "                   *  *  *  *  \n",
      "                  *  *  *  *  *  \n",
      "                 *  *  *  *  *  *  \n",
      "                *  *  *  *  *  *  *  \n",
      "               *  *  *  *  *  *  *  *  \n",
      "              *  *  *  *  *  *  *  *  *  \n",
      "             *  *  *  *  *  *  *  *  *  *  \n",
      "            *  *  *  *  *  *  *  *  *  *  *  \n",
      "           *  *  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows\"))\n",
    "k=a-2\n",
    "for i in range(a,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print(\"\")\n",
    "    k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"*  \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "bcfc9c07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "*  \n",
      "*  *  \n",
      "*  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(0,a):\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "021c9eb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows 12\n",
      "                      * \n",
      "                    * * \n",
      "                  * * * \n",
      "                * * * * \n",
      "              * * * * * \n",
      "            * * * * * * \n",
      "          * * * * * * * \n",
      "        * * * * * * * * \n",
      "      * * * * * * * * * \n",
      "    * * * * * * * * * * \n",
      "  * * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows \"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "febf4601",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows:12\n",
      "                      *  \n",
      "                    *  *  \n",
      "                  *  *  *  \n",
      "                *  *  *  *  \n",
      "              *  *  *  *  *  \n",
      "            *  *  *  *  *  *  \n",
      "          *  *  *  *  *  *  *  \n",
      "        *  *  *  *  *  *  *  *  \n",
      "      *  *  *  *  *  *  *  *  *  \n",
      "    *  *  *  *  *  *  *  *  *  *  \n",
      "  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows:\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "5cbc68af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "* * * * * * * * * * * * * * \n",
      "* * * * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n",
      "* * * * * * * * * * * \n",
      "* * * * * * * * * * \n",
      "* * * * * * * * * \n",
      "* * * * * * * * \n",
      "* * * * * * * \n",
      "* * * * * * \n",
      "* * * * * \n",
      "* * * * \n",
      "* * * \n",
      "* * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(a+1,0,-1):\n",
    "    for j in range(0,k,-1):\n",
    "        print(end=\" \")\n",
    "    k=k-1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "2ce6b641",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows12\n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  \n",
      "*  *  \n",
      "*  \n",
      "\n"
     ]
    }
   ],
   "source": [
    "a=int(input('enter the number of rows'))\n",
    "for i in range (a+1,0,-1):\n",
    "    for j in range(0,i-1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "b622dc36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  \n",
      "*  *  \n",
      "*  \n",
      "\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(a+1,0,-1):\n",
    "    for j in range(0,i-1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "2738d248",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(0,a):\n",
    "    for j in range(0,a+6):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "55c426b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "                      *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                       *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                        *  *  *  *  *  *  *  *  *  *  *  \n",
      "                         *  *  *  *  *  *  *  *  *  *  \n",
      "                          *  *  *  *  *  *  *  *  *  \n",
      "                           *  *  *  *  *  *  *  *  \n",
      "                            *  *  *  *  *  *  *  \n",
      "                             *  *  *  *  *  *  \n",
      "                              *  *  *  *  *  \n",
      "                               *  *  *  *  \n",
      "                                *  *  *  \n",
      "                                 *  *  \n",
      "                                  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(a,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "ac273770",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "                      * \n",
      "                     * * \n",
      "                    * * * \n",
      "                   * * * * \n",
      "                  * * * * * \n",
      "                 * * * * * * \n",
      "                * * * * * * * \n",
      "               * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n",
      "          * * * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "               * * * * * * * * \n",
      "                * * * * * * * \n",
      "                 * * * * * * \n",
      "                  * * * * * \n",
      "                   * * * * \n",
      "                    * * * \n",
      "                     * * \n",
      "                      * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "k=a-2\n",
    "for i in range(a,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "20013c45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "                      * \n",
      "                     * * \n",
      "                    * * * \n",
      "                   * * * * \n",
      "                  * * * * * \n",
      "                 * * * * * * \n",
      "                * * * * * * * \n",
      "               * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n",
      "          * * * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "               * * * * * * * * \n",
      "                * * * * * * * \n",
      "                 * * * * * * \n",
      "                  * * * * * \n",
      "                   * * * * \n",
      "                    * * * \n",
      "                     * * \n",
      "                      * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "k=a-2\n",
    "for i in range(a,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "aee2e3ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "          * * * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "               * * * * * * * * \n",
      "                * * * * * * * \n",
      "                 * * * * * * \n",
      "                  * * * * * \n",
      "                   * * * * \n",
      "                    * * * \n",
      "                     * * \n",
      "                      * \n",
      "                      * \n",
      "                     * * \n",
      "                    * * * \n",
      "                   * * * * \n",
      "                  * * * * * \n",
      "                 * * * * * * \n",
      "                * * * * * * * \n",
      "               * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a-2\n",
    "for i in range(a,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "a1901bd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of rows :12\n",
      "*  \n",
      "*  *  \n",
      "*  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"number of rows :\"))\n",
    "for i in range(0,a):\n",
    "    for j in range (0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "87c6844c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of rows :12\n",
      "                      * \n",
      "                    * * \n",
      "                  * * * \n",
      "                * * * * \n",
      "              * * * * * \n",
      "            * * * * * * \n",
      "          * * * * * * * \n",
      "        * * * * * * * * \n",
      "      * * * * * * * * * \n",
      "    * * * * * * * * * * \n",
      "  * * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "559f3906",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of rows :12\n",
      "                      *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                    *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "              *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "            *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "          *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "        *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "      *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "    *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range(0,a+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "194b06f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of rows :12\n",
      "                      *  \n",
      "                    *  *  \n",
      "                  *  *  *  \n",
      "                *  *  *  *  \n",
      "              *  *  *  *  *  \n",
      "            *  *  *  *  *  *  \n",
      "          *  *  *  *  *  *  *  \n",
      "        *  *  *  *  *  *  *  *  \n",
      "      *  *  *  *  *  *  *  *  *  \n",
      "    *  *  *  *  *  *  *  *  *  *  \n",
      "  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ac16ac8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :10\n",
      "\n",
      "1 \n",
      "2 2 \n",
      "3 3 3 \n",
      "4 4 4 4 \n",
      "5 5 5 5 5 \n",
      "6 6 6 6 6 6 \n",
      "7 7 7 7 7 7 7 \n",
      "8 8 8 8 8 8 8 8 \n",
      "9 9 9 9 9 9 9 9 9 \n",
      "10 10 10 10 10 10 10 10 10 10 \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(a+1):\n",
    "    for j in range(i):\n",
    "        print(i,end=\" \")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "311c7c4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :13\n",
      "\n",
      "1 \n",
      "2 2 \n",
      "3 3 3 \n",
      "4 4 4 4 \n",
      "5 5 5 5 5 \n",
      "6 6 6 6 6 6 \n",
      "7 7 7 7 7 7 7 \n",
      "8 8 8 8 8 8 8 8 \n",
      "9 9 9 9 9 9 9 9 9 \n",
      "10 10 10 10 10 10 10 10 10 10 \n",
      "11 11 11 11 11 11 11 11 11 11 11 \n",
      "12 12 12 12 12 12 12 12 12 12 12 12 \n",
      "13 13 13 13 13 13 13 13 13 13 13 13 13 \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(a+1):\n",
    "    for j in range(i):\n",
    "        print(i,end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ed3655d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :32\n",
      "1  \n",
      "1  2  \n",
      "1  2  3  \n",
      "1  2  3  4  \n",
      "1  2  3  4  5  \n",
      "1  2  3  4  5  6  \n",
      "1  2  3  4  5  6  7  \n",
      "1  2  3  4  5  6  7  8  \n",
      "1  2  3  4  5  6  7  8  9  \n",
      "1  2  3  4  5  6  7  8  9  10  \n",
      "1  2  3  4  5  6  7  8  9  10  11  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  \n",
      "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(1,a+1):\n",
    "    for j in range(1,i+1):\n",
    "        print(j,end=\"  \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c5dcd8ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "\n",
      "1 \n",
      "2 2 \n",
      "3 3 3 \n",
      "4 4 4 4 \n",
      "5 5 5 5 5 \n",
      "6 6 6 6 6 6 \n",
      "7 7 7 7 7 7 7 \n",
      "8 8 8 8 8 8 8 8 \n",
      "9 9 9 9 9 9 9 9 9 \n",
      "10 10 10 10 10 10 10 10 10 10 \n",
      "11 11 11 11 11 11 11 11 11 11 11 \n",
      "12 12 12 12 12 12 12 12 12 12 12 12 \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(a+1):\n",
    "    for j in range(i):\n",
    "        print(i,end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c6e81b8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "1 \n",
      "1 2 \n",
      "1 2 3 \n",
      "1 2 3 4 \n",
      "1 2 3 4 5 \n",
      "1 2 3 4 5 6 \n",
      "1 2 3 4 5 6 7 \n",
      "1 2 3 4 5 6 7 8 \n",
      "1 2 3 4 5 6 7 8 9 \n",
      "1 2 3 4 5 6 7 8 9 10 \n",
      "1 2 3 4 5 6 7 8 9 10 11 \n",
      "1 2 3 4 5 6 7 8 9 10 11 12 \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(1,a+1):\n",
    "    for j in range(1,i+1):\n",
    "        print(j,end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "903ce0e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :10\n",
      "\n",
      "1 \n",
      "2 2 \n",
      "3 3 3 \n",
      "4 4 4 4 \n",
      "5 5 5 5 5 \n",
      "6 6 6 6 6 6 \n",
      "7 7 7 7 7 7 7 \n",
      "8 8 8 8 8 8 8 8 \n",
      "9 9 9 9 9 9 9 9 9 \n",
      "10 10 10 10 10 10 10 10 10 10 \n",
      "1 \n",
      "1 2 \n",
      "1 2 3 \n",
      "1 2 3 4 \n",
      "1 2 3 4 5 \n",
      "1 2 3 4 5 6 \n",
      "1 2 3 4 5 6 7 \n",
      "1 2 3 4 5 6 7 8 \n",
      "1 2 3 4 5 6 7 8 9 \n",
      "1 2 3 4 5 6 7 8 9 10 \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(a+1):\n",
    "    for j in range(i):\n",
    "        print(i,end=\" \")\n",
    "    print()\n",
    "for i in range(1,a+1):\n",
    "    for j in range(1,i+1):\n",
    "        print(j,end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3337416d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "\n",
      "*  \n",
      "*  *  \n",
      "*  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input (\"enter the number of rows :\"))\n",
    "for i in range(0,a):\n",
    "    for j in range(0,i):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7870b497",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "                      * \n",
      "                    * * \n",
      "                  * * * \n",
      "                * * * * \n",
      "              * * * * * \n",
      "            * * * * * * \n",
      "          * * * * * * * \n",
      "        * * * * * * * * \n",
      "      * * * * * * * * * \n",
      "    * * * * * * * * * * \n",
      "  * * * * * * * * * * * \n",
      "* * * * * * * * * * * * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range (0,a):\n",
    "    for  j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1139f167",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "                      *  \n",
      "                    *  *  \n",
      "                  *  *  *  \n",
      "                *  *  *  *  \n",
      "              *  *  *  *  *  \n",
      "            *  *  *  *  *  *  \n",
      "          *  *  *  *  *  *  *  \n",
      "        *  *  *  *  *  *  *  *  \n",
      "      *  *  *  *  *  *  *  *  *  \n",
      "    *  *  *  *  *  *  *  *  *  *  \n",
      "  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "39a65b93",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "                      *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                    *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "              *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "            *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "          *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "        *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "      *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "    *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "  *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-2\n",
    "    for j in range(0,a+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c5b44f45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "                      *  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                       *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "                        *  *  *  *  *  *  *  *  *  *  *  \n",
      "                         *  *  *  *  *  *  *  *  *  *  \n",
      "                          *  *  *  *  *  *  *  *  *  \n",
      "                           *  *  *  *  *  *  *  *  \n",
      "                            *  *  *  *  *  *  *  \n",
      "                             *  *  *  *  *  *  \n",
      "                              *  *  *  *  *  \n",
      "                               *  *  *  *  \n",
      "                                *  *  *  \n",
      "                                 *  *  \n",
      "                                  *  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(a+1,0,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "73fae404",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "           * * * * * * * * * * * * * \n",
      "            * * * * * * * * * * * * \n",
      "             * * * * * * * * * * * \n",
      "              * * * * * * * * * * \n",
      "               * * * * * * * * * \n",
      "                * * * * * * * * \n",
      "                 * * * * * * * \n",
      "                  * * * * * * \n",
      "                   * * * * * \n",
      "                    * * * * \n",
      "                     * * * \n",
      "                      * * \n",
      "                       * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a-2\n",
    "for i in range(a,-1,-1):\n",
    "    for j in range(k,-1,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "06271d32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows  :12\n",
      "*  \n",
      "*  *  \n",
      "*  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  *  \n",
      "*  *  *  *  *  *  \n",
      "*  *  *  *  *  \n",
      "*  *  *  *  \n",
      "*  *  *  \n",
      "*  *  \n",
      "*  \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows  :\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\"\")\n",
    "    k=k-2\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()\n",
    "k=a-2\n",
    "for i in range(a+1,0,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\"\")\n",
    "    k=k+1\n",
    "    for j in range(0,i):\n",
    "        print(\"* \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "8a30521f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "                      * \n",
      "                     * * \n",
      "                    * * * \n",
      "                   * * * * \n",
      "                  * * * * * \n",
      "                 * * * * * * \n",
      "                * * * * * * * \n",
      "               * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n",
      "          * * * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "               * * * * * * * * \n",
      "                * * * * * * * \n",
      "                 * * * * * * \n",
      "                  * * * * * \n",
      "                   * * * * \n",
      "                    * * * \n",
      "                     * * \n",
      "                      * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "k=a-2\n",
    "for i in range(a+1,0,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "70eb6236",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "          * * * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "               * * * * * * * * \n",
      "                * * * * * * * \n",
      "                 * * * * * * \n",
      "                  * * * * * \n",
      "                   * * * * \n",
      "                    * * * \n",
      "                     * * \n",
      "                      * \n",
      "                      * \n",
      "                     * * \n",
      "                    * * * \n",
      "                   * * * * \n",
      "                  * * * * * \n",
      "                 * * * * * * \n",
      "                * * * * * * * \n",
      "               * * * * * * * * \n",
      "              * * * * * * * * * \n",
      "             * * * * * * * * * * \n",
      "            * * * * * * * * * * * \n",
      "           * * * * * * * * * * * * \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "k=a-2\n",
    "for i in range(a+1,0,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+1\n",
    "    for j in range(0,i):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "k=a*2-2\n",
    "for i in range(0,a):\n",
    "    for j in range(0,k):\n",
    "        print(end=\" \")\n",
    "    k=k-1\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "419a7125",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "\n",
      "1 \n",
      "2 2 \n",
      "3 3 3 \n",
      "4 4 4 4 \n",
      "5 5 5 5 5 \n",
      "6 6 6 6 6 6 \n",
      "7 7 7 7 7 7 7 \n",
      "8 8 8 8 8 8 8 8 \n",
      "9 9 9 9 9 9 9 9 9 \n",
      "10 10 10 10 10 10 10 10 10 10 \n",
      "11 11 11 11 11 11 11 11 11 11 11 \n",
      "12 12 12 12 12 12 12 12 12 12 12 12 \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(a+1):\n",
    "    for j in range(i):\n",
    "        print(i,end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "1d3b627e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number of rows :12\n",
      "1 \n",
      "1 2 \n",
      "1 2 3 \n",
      "1 2 3 4 \n",
      "1 2 3 4 5 \n",
      "1 2 3 4 5 6 \n",
      "1 2 3 4 5 6 7 \n",
      "1 2 3 4 5 6 7 8 \n",
      "1 2 3 4 5 6 7 8 9 \n",
      "1 2 3 4 5 6 7 8 9 10 \n",
      "1 2 3 4 5 6 7 8 9 10 11 \n",
      "1 2 3 4 5 6 7 8 9 10 11 12 \n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the number of rows :\"))\n",
    "for i in range(1,a+1):\n",
    "    for j in range(1,i+1):\n",
    "        print(j,end=\" \")\n",
    "    print()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  },
  "vscode": {
   "interpreter": {
    "hash": "52634da84371cba311ea128a5ea7cdc41ff074b781779e754b270ff9f8153cee"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
