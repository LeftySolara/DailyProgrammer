// [2015-03-23] Challenge #207 [Easy] Bioinformatics 1: DNA Replication
// http://www.reddit.com/r/dailyprogrammer/comments/2zyipu/20150323_challenge_207_easy_bioinformatics_1_dna/


using System;
using System.Collections.Generic;

public class Replicator
{
	protected Dictionary<char, char> basePairs = new Dictionary<char, char>()
	{
		{'A', 'T'},
		{'T', 'A'},
		{'G', 'C'},
		{'C', 'G'}
	};

	public string replicate(string strand)
	{
		string original = strand;
		string replication = "";

		foreach (char elem in original) 
		{
			if (elem == ' ') {
				replication += " ";
				continue;
			}
			replication += basePairs[elem];
		}

		return replication;

	}
}

public class ReplicationTest
{
	static void Main(string[] args)
	{
		string strand = "A A T G C C T A T G G C";
		Replicator rep = new Replicator();

		Console.WriteLine(strand);
		Console.WriteLine(rep.replicate(strand));
	}
}