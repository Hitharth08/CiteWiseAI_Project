class CitationEngine:

    @staticmethod
    def format(chunks):
        """
        Format retrieved chunks into a readable citation block.
        """
        citations = []

        for i, chunk in enumerate(chunks, start=1):
            citations.append(
                f"Source {i}\n"
                f"{'-'*40}\n"
                f"{chunk}\n"
            )

        return "\n\n".join(citations)
